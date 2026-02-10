import sys
import os
import pymysql as conn
from hashlib import sha256
from dotenv import load_dotenv
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QLabel, QComboBox, QTableWidget, QTableWidgetItem,
    QDialog, QMessageBox, QSpinBox, QDoubleSpinBox, QTextEdit, QHeaderView,
    QTabWidget, QFormLayout
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QColor, QIcon

# Cargar variables de entorno
load_dotenv()

# Configuración de la base de datos (desde variables de entorno)
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'inventario-ortizcruzbrian-0474.c.aivencloud.com'),
    'port': int(os.getenv('DB_PORT', '14788')),
    'user': os.getenv('DB_USER', 'avnadmin'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'defaultdb'),
    'charset': 'utf8mb4',
    'ssl': {
        'ca': 'ca.pem'
    }
}

DB_CONFIG2 ={
    'host' : 'localhost',
    'port' : 3307,
    'user' : 'root',
    'password' : '',
    'database' : 'Inventario'

}

def execute_query(query, params=None, use_db=True):
    config = DB_CONFIG if use_db else {k: v for k, v in DB_CONFIG.items() if k != 'database'}
    connection = conn.connect(**config)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
        connection.commit()
    finally:
        connection.close()

def fetch_query(query, params=None):
    connection = conn.connect(**DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
    finally:
        connection.close()

def create_database_if_not_exists():
    query = f"CREATE DATABASE IF NOT EXISTS `{DB_CONFIG['database']}`;"
    execute_query(query, use_db=False)
    print(f"Base de datos '{DB_CONFIG['database']}' verificada o creada exitosamente.")

def create_tables():
    queries = [
        """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            role ENUM('admin', 'employee') DEFAULT 'employee'
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS categories (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) UNIQUE NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            category_id INT,
            price DECIMAL(10, 2),
            stock INT DEFAULT 0,
            image_path VARCHAR(500),
            FOREIGN KEY (category_id) REFERENCES categories(id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS movements (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_id INT NOT NULL,
            type ENUM('entrada', 'salida') NOT NULL,
            quantity INT NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            description TEXT,
            FOREIGN KEY (product_id) REFERENCES products(id)
        );
        """
    ]
    for query in queries:
        execute_query(query)
    print("Tablas creadas exitosamente.")

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def create_admin_user_if_not_exists():
    connection = conn.connect(**DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM users WHERE username = 'admin';")
            count = cursor.fetchone()[0]
            if count == 0:
                cursor.execute(
                    "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, 'admin');",
                    ("admin", hash_password("admin"))
                )
                connection.commit()
                print("✅ Usuario 'admin' creado exitosamente.")
            else:
                print("ℹ️ Usuario 'admin' ya existe.")
    finally:
        connection.close()

def get_user_by_username(username):
    connection = conn.connect(**DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, username, password_hash, role FROM users WHERE username = %s;", (username,))
            result = cursor.fetchone()
            if result:
                return {
                    'id': result[0],
                    'username': result[1],
                    'password_hash': result[2],
                    'role': result[3]
                }
            return None
    finally:
        connection.close()

def get_all_categories():
    return fetch_query("SELECT id, name FROM categories ORDER BY name;")

def get_all_products():
    return fetch_query("""
        SELECT p.id, p.name, p.description, c.name, p.price, p.stock, p.image_path
        FROM products p
        LEFT JOIN categories c ON p.category_id = c.id
        ORDER BY p.name;
    """)

def get_all_movements():
    return fetch_query("""
        SELECT m.id, p.name, m.type, m.quantity, m.date, m.description
        FROM movements m
        LEFT JOIN products p ON m.product_id = p.id
        ORDER BY m.date DESC;
    """)

def create_category(name):
    execute_query("INSERT INTO categories (name) VALUES (%s);", (name,))
    print(f"Categoría '{name}' creada exitosamente.")

def update_category(category_id, name):
    execute_query("UPDATE categories SET name = %s WHERE id = %s;", (name, category_id))
    print(f"Categoría actualizada exitosamente.")

def delete_category(category_id):
    execute_query("DELETE FROM categories WHERE id = %s;", (category_id,))
    print(f"Categoría eliminada exitosamente.")

def create_product(name, description, category_id, price, stock=0, image_path=None):
    execute_query(
        "INSERT INTO products (name, description, category_id, price, stock, image_path) VALUES (%s, %s, %s, %s, %s, %s);",
        (name, description, category_id, price, stock, image_path)
    )
    print(f"Producto '{name}' creado exitosamente.")

def update_product(product_id, name, description, category_id, price, stock, image_path):
    execute_query(
        "UPDATE products SET name = %s, description = %s, category_id = %s, price = %s, stock = %s, image_path = %s WHERE id = %s;",
        (name, description, category_id, price, stock, image_path, product_id)
    )
    print(f"Producto actualizado exitosamente.")

def delete_product(product_id):
    execute_query("DELETE FROM products WHERE id = %s;", (product_id,))
    print(f"Producto eliminado exitosamente.")

def register_movement(product_id, movement_type, quantity, description=""):
    connection = conn.connect(**DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            if movement_type == "entrada":
                cursor.execute("UPDATE products SET stock = stock + %s WHERE id = %s;", (quantity, product_id))
            elif movement_type == "salida":
                cursor.execute("UPDATE products SET stock = stock - %s WHERE id = %s;", (quantity, product_id))
            
            cursor.execute(
                "INSERT INTO movements (product_id, type, quantity, description) VALUES (%s, %s, %s, %s);",
                (product_id, movement_type, quantity, description)
            )
        connection.commit()
        print(f"Movimiento registrado exitosamente.")
    finally:
        connection.close()

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Inventario - Login")
        self.setGeometry(100, 100, 500, 300)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        
        title = QLabel("Sistema de Inventario")
        title.setFont(QFont("Arial", 24, QFont.Bold))
        layout.addWidget(title)
        
        form_layout = QFormLayout()
        
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        
        form_layout.addRow("Usuario:", self.username_input)
        form_layout.addRow("Contraseña:", self.password_input)
        
        layout.addLayout(form_layout)
        
        login_btn = QPushButton("Iniciar Sesión")
        login_btn.clicked.connect(self.handle_login)
        layout.addWidget(login_btn)
        
        central_widget.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        if not username or not password:
            QMessageBox.warning(self, "Error", "Usuario y contraseña son obligatorios.")
            return
        
        user = get_user_by_username(username)
        if user and user['password_hash'] == hash_password(password):
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            QMessageBox.critical(self, "Error", "Credenciales incorrectas.")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Inventario")
        self.setGeometry(100, 100, 1200, 700)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        
        title = QLabel("Sistema de Inventario")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        layout.addWidget(title)
        
        tabs = QTabWidget()
        tabs.addTab(self.create_products_tab(), "Productos")
        tabs.addTab(self.create_categories_tab(), "Categorías")
        tabs.addTab(self.create_movements_tab(), "Movimientos")
        
        layout.addWidget(tabs)
        
        logout_btn = QPushButton("Cerrar Sesión")
        logout_btn.clicked.connect(self.handle_logout)
        layout.addWidget(logout_btn)
        
        central_widget.setLayout(layout)

    def create_products_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        form_layout = QFormLayout()
        
        self.product_name = QLineEdit()
        self.product_description = QTextEdit()
        self.product_category = QComboBox()
        self.product_price = QDoubleSpinBox()
        self.product_price.setMaximum(999999.99)
        self.product_stock = QSpinBox()
        self.product_stock.setMaximum(999999)
        self.product_image = QLineEdit()
        
        self.load_categories_combo()
        
        form_layout.addRow("Nombre:", self.product_name)
        form_layout.addRow("Descripción:", self.product_description)
        form_layout.addRow("Categoría:", self.product_category)
        form_layout.addRow("Precio:", self.product_price)
        form_layout.addRow("Stock:", self.product_stock)
        form_layout.addRow("Imagen:", self.product_image)
        
        layout.addLayout(form_layout)
        
        button_layout = QHBoxLayout()
        add_btn = QPushButton("Agregar Producto")
        add_btn.clicked.connect(self.add_product)
        update_btn = QPushButton("Actualizar Seleccionado")
        update_btn.clicked.connect(self.update_product)
        delete_btn = QPushButton("Eliminar Seleccionado")
        delete_btn.clicked.connect(self.delete_product)
        clear_btn = QPushButton("Limpiar")
        clear_btn.clicked.connect(self.clear_product_form)
        
        button_layout.addWidget(add_btn)
        button_layout.addWidget(update_btn)
        button_layout.addWidget(delete_btn)
        button_layout.addWidget(clear_btn)
        layout.addLayout(button_layout)
        
        self.products_table = QTableWidget()
        self.products_table.setColumnCount(7)
        self.products_table.setHorizontalHeaderLabels(["ID", "Nombre", "Descripción", "Categoría", "Precio", "Stock", "Imagen"])
        self.products_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.products_table.itemSelectionChanged.connect(self.load_product_to_form)
        layout.addWidget(self.products_table)
        
        self.refresh_products_table()
        
        widget.setLayout(layout)
        return widget

    def create_categories_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        form_layout = QFormLayout()
        
        self.category_name = QLineEdit()
        form_layout.addRow("Nombre:", self.category_name)
        
        layout.addLayout(form_layout)
        
        button_layout = QHBoxLayout()
        add_btn = QPushButton("Agregar Categoría")
        add_btn.clicked.connect(self.add_category)
        update_btn = QPushButton("Actualizar Seleccionada")
        update_btn.clicked.connect(self.update_category)
        delete_btn = QPushButton("Eliminar Seleccionada")
        delete_btn.clicked.connect(self.delete_category)
        clear_btn = QPushButton("Limpiar")
        clear_btn.clicked.connect(lambda: self.category_name.clear())
        
        button_layout.addWidget(add_btn)
        button_layout.addWidget(update_btn)
        button_layout.addWidget(delete_btn)
        button_layout.addWidget(clear_btn)
        layout.addLayout(button_layout)
        
        self.categories_table = QTableWidget()
        self.categories_table.setColumnCount(2)
        self.categories_table.setHorizontalHeaderLabels(["ID", "Nombre"])
        self.categories_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.categories_table.itemSelectionChanged.connect(self.load_category_to_form)
        layout.addWidget(self.categories_table)
        
        self.refresh_categories_table()
        
        widget.setLayout(layout)
        return widget

    def create_movements_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        form_layout = QFormLayout()
        
        self.movement_product = QComboBox()
        self.movement_type = QComboBox()
        self.movement_type.addItems(["entrada", "salida"])
        self.movement_quantity = QSpinBox()
        self.movement_quantity.setMaximum(999999)
        self.movement_description = QTextEdit()
        
        self.load_products_combo()
        
        form_layout.addRow("Producto:", self.movement_product)
        form_layout.addRow("Tipo:", self.movement_type)
        form_layout.addRow("Cantidad:", self.movement_quantity)
        form_layout.addRow("Descripción:", self.movement_description)
        
        layout.addLayout(form_layout)
        
        register_btn = QPushButton("Registrar Movimiento")
        register_btn.clicked.connect(self.register_movement)
        layout.addWidget(register_btn)
        
        self.movements_table = QTableWidget()
        self.movements_table.setColumnCount(6)
        self.movements_table.setHorizontalHeaderLabels(["ID", "Producto", "Tipo", "Cantidad", "Fecha", "Descripción"])
        self.movements_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.movements_table)
        
        self.refresh_movements_table()
        
        widget.setLayout(layout)
        return widget

    def load_categories_combo(self):
        self.product_category.clear()
        categories = get_all_categories()
        for cat in categories:
            self.product_category.addItem(cat[1], cat[0])

    def load_products_combo(self):
        self.movement_product.clear()
        products = get_all_products()
        for prod in products:
            self.movement_product.addItem(prod[1], prod[0])

    def refresh_products_table(self):
        products = get_all_products()
        self.products_table.setRowCount(len(products))
        for row, product in enumerate(products):
            for col, data in enumerate(product):
                self.products_table.setItem(row, col, QTableWidgetItem(str(data)))

    def refresh_categories_table(self):
        categories = get_all_categories()
        self.categories_table.setRowCount(len(categories))
        for row, category in enumerate(categories):
            for col, data in enumerate(category):
                self.categories_table.setItem(row, col, QTableWidgetItem(str(data)))

    def refresh_movements_table(self):
        movements = get_all_movements()
        self.movements_table.setRowCount(len(movements))
        for row, movement in enumerate(movements):
            for col, data in enumerate(movement):
                self.movements_table.setItem(row, col, QTableWidgetItem(str(data)))

    def load_product_to_form(self):
        selected = self.products_table.selectedItems()
        if selected:
            row = self.products_table.row(selected[0])
            self.product_name.setText(self.products_table.item(row, 1).text())
            self.product_description.setText(self.products_table.item(row, 2).text())
            category_text = self.products_table.item(row, 3).text()
            index = self.product_category.findText(category_text)
            if index >= 0:
                self.product_category.setCurrentIndex(index)
            self.product_price.setValue(float(self.products_table.item(row, 4).text()))
            self.product_stock.setValue(int(self.products_table.item(row, 5).text()))
            self.product_image.setText(self.products_table.item(row, 6).text())

    def load_category_to_form(self):
        selected = self.categories_table.selectedItems()
        if selected:
            row = self.categories_table.row(selected[0])
            self.category_name.setText(self.categories_table.item(row, 1).text())

    def add_product(self):
        name = self.product_name.text()
        if not name:
            QMessageBox.warning(self, "Error", "El nombre es obligatorio.")
            return
        
        try:
            create_product(
                name,
                self.product_description.toPlainText(),
                self.product_category.currentData(),
                self.product_price.value(),
                self.product_stock.value(),
                self.product_image.text()
            )
            self.refresh_products_table()
            self.clear_product_form()
            QMessageBox.information(self, "Éxito", "Producto agregado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al agregar producto: {str(e)}")

    def update_product(self):
        selected = self.products_table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Error", "Selecciona un producto para actualizar.")
            return
        
        row = self.products_table.row(selected[0])
        product_id = int(self.products_table.item(row, 0).text())
        
        try:
            update_product(
                product_id,
                self.product_name.text(),
                self.product_description.toPlainText(),
                self.product_category.currentData(),
                self.product_price.value(),
                self.product_stock.value(),
                self.product_image.text()
            )
            self.refresh_products_table()
            self.clear_product_form()
            QMessageBox.information(self, "Éxito", "Producto actualizado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al actualizar producto: {str(e)}")

    def delete_product(self):
        selected = self.products_table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Error", "Selecciona un producto para eliminar.")
            return
        
        reply = QMessageBox.question(self, "Confirmar", "¿Estás seguro de que deseas eliminar este producto?")
        if reply == QMessageBox.Yes:
            row = self.products_table.row(selected[0])
            product_id = int(self.products_table.item(row, 0).text())
            try:
                delete_product(product_id)
                self.refresh_products_table()
                self.clear_product_form()
                QMessageBox.information(self, "Éxito", "Producto eliminado correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al eliminar producto: {str(e)}")

    def clear_product_form(self):
        self.product_name.clear()
        self.product_description.clear()
        self.product_price.setValue(0)
        self.product_stock.setValue(0)
        self.product_image.clear()

    def add_category(self):
        name = self.category_name.text()
        if not name:
            QMessageBox.warning(self, "Error", "El nombre es obligatorio.")
            return
        
        try:
            create_category(name)
            self.refresh_categories_table()
            self.load_categories_combo()
            self.category_name.clear()
            QMessageBox.information(self, "Éxito", "Categoría agregada correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al agregar categoría: {str(e)}")

    def update_category(self):
        selected = self.categories_table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Error", "Selecciona una categoría para actualizar.")
            return
        
        row = self.categories_table.row(selected[0])
        category_id = int(self.categories_table.item(row, 0).text())
        
        try:
            update_category(category_id, self.category_name.text())
            self.refresh_categories_table()
            self.load_categories_combo()
            self.category_name.clear()
            QMessageBox.information(self, "Éxito", "Categoría actualizada correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al actualizar categoría: {str(e)}")

    def delete_category(self):
        selected = self.categories_table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Error", "Selecciona una categoría para eliminar.")
            return
        
        reply = QMessageBox.question(self, "Confirmar", "¿Estás seguro de que deseas eliminar esta categoría?")
        if reply == QMessageBox.Yes:
            row = self.categories_table.row(selected[0])
            category_id = int(self.categories_table.item(row, 0).text())
            try:
                delete_category(category_id)
                self.refresh_categories_table()
                self.load_categories_combo()
                self.category_name.clear()
                QMessageBox.information(self, "Éxito", "Categoría eliminada correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al eliminar categoría: {str(e)}")

    def register_movement(self):
        try:
            register_movement(
                self.movement_product.currentData(),
                self.movement_type.currentText(),
                self.movement_quantity.value(),
                self.movement_description.toPlainText()
            )
            self.refresh_movements_table()
            self.refresh_products_table()
            self.movement_quantity.setValue(0)
            self.movement_description.clear()
            QMessageBox.information(self, "Éxito", "Movimiento registrado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al registrar movimiento: {str(e)}")

    def handle_logout(self):
        reply = QMessageBox.question(self, "Confirmar", "¿Deseas cerrar sesión?")
        if reply == QMessageBox.Yes:
            self.login_window = LoginWindow()
            self.login_window.show()
            self.close()

def main():
    create_database_if_not_exists()
    create_tables()
    create_admin_user_if_not_exists()
    
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()