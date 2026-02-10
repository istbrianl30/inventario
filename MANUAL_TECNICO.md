# 🔧 Manual Técnico - Sistema de Inventario (v2.0)

**Versión:** 2.0  
**Última actualización:** Febrero 2026  
**Nivel:** Avanzado / Desarrollo  
**Audiencia:** Desarrolladores, Administradores de IT, DevOps

---

## 📋 Índice Detallado

1. [Introducción Técnica](#introducción-técnica)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Stack Tecnológico](#stack-tecnológico)
4. [Requisitos de Desarrollo](#requisitos-de-desarrollo)
5. [Instalación Detallada](#instalación-detallada)
6. [Estructura del Proyecto](#estructura-del-proyecto)
7. [Base de Datos](#base-de-datos)
8. [API y Funciones Documentadas](#api-y-funciones-documentadas)
9. [Configuración Avanzada](#configuración-avanzada)
10. [Build & Deployment](#build--deployment)
11. [Testing y QA](#testing-y-qa)
12. [Debugging Avanzado](#debugging-avanzado)
13. [Seguridad](#seguridad)
14. [Optimización](#optimización)
15. [Troubleshooting Técnico](#troubleshooting-técnico)
16. [Roadmap Futuro](#roadmap-futuro)

---

## Introducción Técnica

El **Sistema de Inventario** es una aplicación **full-stack** profesional desarrollada con tecnologías modernas:

**Características técnicas principales:**
- ✅ Interfaz nativa del SO (PySide6/Qt6)
- ✅ BD relacional con integridad referencial
- ✅ Autenticación con hash criptográfico
- ✅ Conexión segura SSL/TLS
- ✅ Arquitectura en capas (MVC)
- ✅ Validación en múltiples niveles
- ✅ Caché de datos local
- ✅ Logging completo

---

## Arquitectura del Sistema

### Diagrama de Capas

```
┌──────────────────────────────────────────────┐
│          CAPA DE PRESENTACIÓN (UI)           │
│  ┌────────────────────────────────────────┐  │
│  │ LoginWindow     MainWindow              │  │
│  │ - Login        - Products Tab           │  │
│  │ - Validación   - Categories Tab         │  │
│  │                - Movements Tab          │  │
│  └────────────────────────────────────────┘  │
└───────────────────┬──────────────────────────┘
                    │ Qt Signals/Slots
┌───────────────────▼──────────────────────────┐
│    CAPA DE LÓGICA DE NEGOCIO                 │
│  ┌────────────────────────────────────────┐  │
│  │ - hash_password()                       │  │
│  │ - Validaciones                          │  │
│  │ - Operaciones CRUD                      │  │
│  │ - Gestión de transacciones              │  │
│  │ - Estadísticas                          │  │
│  └────────────────────────────────────────┘  │
└───────────────────┬──────────────────────────┘
                    │ SQL Queries
┌───────────────────▼──────────────────────────┐
│  CAPA DE ACCESO A DATOS (DAL)                │
│  ┌────────────────────────────────────────┐  │
│  │ - execute_query()                       │  │
│  │ - fetch_query()                         │  │
│  │ - Connection pooling                    │  │
│  │ - Error handling                        │  │
│  └────────────────────────────────────────┘  │
└───────────────────┬──────────────────────────┘
                    │ MySQL Protocol / SSL
┌───────────────────▼──────────────────────────┐
│       CAPA DE DATOS (AIVEN CLOUD)            │
│  ┌────────────────────────────────────────┐  │
│  │ MySQL Database                          │  │
│  │ - users                                 │  │
│  │ - categories                            │  │
│  │ - products                              │  │
│  │ - movements                             │  │
│  │ - Backups automáticos                   │  │
│  └────────────────────────────────────────┘  │
└──────────────────────────────────────────────┘
```

---

## Stack Tecnológico

| Componente | Tecnología | Versión | Propósito |
|------------|-----------|---------|----------|
| **Frontend** | PySide6 | 6.7.1+ | Interfaz gráfica nativa |
| **Backend** | Python | 3.9+ | Lógica de negocios |
| **BD** | MySQL | 5.7+ | Almacenamiento persistente |
| **Servidor BD** | Aiven Cloud | - | Hosting en la nube |
| **Build** | PyInstaller | 6.1.0+ | Generación ejecutables |
| **Versioning** | Git | 2.0+ | Control de código |
| **Testing** | pytest | 7.0+ | Unit tests |
| **Documentación** | Markdown | - | Docs y manuales |

---

## Requisitos de Desarrollo

### Hardware Mínimo
```
- CPU: 2 cores (Intel i3 o equivalente)
- RAM: 4 GB
- Almacenamiento: 500 MB libres
- Monitor: 1024x768 mínimo
```

### Hardware Recomendado
```
- CPU: 4 cores (Intel i7 o equivalente)
- RAM: 8 GB
- Almacenamiento: 2 GB SSD
- Monitor: 1920x1080 o superior
```

### Software Necesario
```
✓ Python 3.9+ (https://www.python.org)
✓ Git 2.0+ (https://git-scm.com)
✓ Visual Studio Code (https://code.visualstudio.com)
✓ MySQL Workbench (https://dev.mysql.com/downloads/workbench/)
✓ Postman (opcional, para testing API futura)
```

### IDE Recomendadas
```
1. Visual Studio Code (Recomendado)
   - Extensiones: Python, Pylance, PyLance
   
2. PyCharm Community Edition
   - Intellisense integrado
   
3. Visual Studio 2022 Community
   - Debug avanzado
```

---

## Instalación Detallada
- **Frontend:** PySide6 (Framework Qt para Python)
- **Backend:** Python 3.9+
- **Base de Datos:** MySQL en la nube (Aiven)
- **Seguridad:** SSL/TLS con certificado ca.pem

**Stack Tecnológico:**
```
┌─────────────────────────────────────┐
│     Interfaz de Usuario (UI)        │
│         PySide6 / Qt6               │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│      Lógica de Negocio (BL)         │
│       Python 3.9+                   │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│      Acceso a Datos (DAL)           │
│       PyMySQL                       │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│     Base de Datos MySQL en Nube     │
│        (Aiven Cloud)                │
└─────────────────────────────────────┘
```

---

## Arquitectura del Sistema

### Componentes Principales

#### 1. Capa de Presentación (UI)
- `LoginWindow`: Autenticación de usuarios
- `MainWindow`: Ventana principal con tabs
- Widgets específicos por funcionalidad

#### 2. Capa de Lógica de Negocio
- Validaciones de datos
- Operaciones CRUD
- Gestión de movimientos

#### 3. Capa de Acceso a Datos
- Conexión a base de datos
- Ejecución de queries
- Manejo de transacciones

#### 4. Base de Datos
- Tablas: users, categories, products, movements
- Relaciones FK: products → categories, movements → products

---

## Requisitos de Desarrollo

### Software Necesario
```
- Python 3.9 o superior
- Git (opcional, para control de versiones)
- Visual Studio Code o IDE similar
- MySQL Workbench (para administración de BD)
```

### Variables de Entorno
```
PYTHONPATH: Debe incluir la carpeta del proyecto
MYSQL_HOST: inventario-ortizcruzbrian-0474.c.aivencloud.com
MYSQL_PORT: 14788
```

---

## Instalación del Entorno

### 1. Clonar/Descargar el Proyecto

```powershell
cd C:\Users\[Usuario]\OneDrive\Documents\Python
git clone https://github.com/istbrianl30/inventario.git
# O descargar el ZIP manualmente
```

### 2. Crear Entorno Virtual (Recomendado)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instalar Dependencias

```powershell
pip install -r requirements.txt
```

### 4. Verificar Instalación

```powershell
python -c "import PySide6; import pymysql; print('✅ Dependencias OK')"
```

### 5. Ejecutar la Aplicación

```powershell
python main.py
```

---

## Estructura del Proyecto

```
Inventario/
├── main.py                      # Archivo principal
├── build.spec                   # Configuración PyInstaller
├── requirements.txt             # Dependencias
├── ca.pem                        # Certificado SSL
├── favicon.ico                   # Icono de aplicación
├── MANUAL_USUARIO.md            # Manual del usuario
├── MANUAL_TECNICO.md            # Este archivo
└── dist/                         # Ejecutables compilados
    └── Inventario/
        └── Inventario.exe       # Ejecutable final
```

---

## Base de Datos

### Configuración de Conexión

**Archivo:** `main.py` líneas 19-28

⚠️ **IMPORTANTE:** Las credenciales NO deben estar en el código. Se cargan desde variables de entorno.

```python
# Cargar variables de entorno
load_dotenv()

# Configuración de la base de datos (desde variables de entorno)
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'inventario-ortizcruzbrian-0474.c.aivencloud.com'),
    'port': int(os.getenv('DB_PORT', '14788')),
    'user': os.getenv('DB_USER', 'avnadmin'),
    'password': os.getenv('DB_PASSWORD', ''),  # Desde .env
    'database': os.getenv('DB_NAME', 'defaultdb'),
    'charset': 'utf8mb4',
    'ssl': {
        'ca': 'ca.pem'
    }
}
```

**Archivo `.env` (NO incluido en Git):**
```
DB_HOST=inventario-ortizcruzbrian-0474.c.aivencloud.com
DB_PORT=14788
DB_USER=avnadmin
DB_PASSWORD=tu_contraseña_aquí
DB_NAME=defaultdb
```

### Esquema de Base de Datos

#### Tabla: users
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('admin', 'employee') DEFAULT 'employee'
);
```

#### Tabla: categories
```sql
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);
```

#### Tabla: products
```sql
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category_id INT,
    price DECIMAL(10, 2),
    stock INT DEFAULT 0,
    image_path VARCHAR(500),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
```

#### Tabla: movements
```sql
CREATE TABLE movements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    type ENUM('entrada', 'salida') NOT NULL,
    quantity INT NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

### Relaciones
```
users (1) ──────────── (N) [No hay relación directa]
categories (1) ──────── (N) products
products (1) ────────── (N) movements
```

---

## API y Funciones

### Funciones de Base de Datos

#### execute_query(query, params=None, use_db=True)
Ejecuta una query que modifica la BD (INSERT, UPDATE, DELETE)

```python
execute_query("INSERT INTO categories (name) VALUES (%s)", ("Electrónica",))
```

#### fetch_query(query, params=None)
Obtiene datos de la BD (SELECT)

```python
results = fetch_query("SELECT * FROM products WHERE id = %s", (1,))
```

### Funciones de Autenticación

#### hash_password(password)
Genera hash SHA256 de la contraseña

```python
hashed = hash_password("micontraseña")
```

#### get_user_by_username(username)
Obtiene datos del usuario

```python
user = get_user_by_username("admin")
# Retorna: {'id': 1, 'username': 'admin', 'password_hash': '...', 'role': 'admin'}
```

### Funciones de Categorías

#### get_all_categories()
Obtiene todas las categorías

```python
categories = get_all_categories()
# Retorna: [(1, 'Electrónica'), (2, 'Ropa'), ...]
```

#### create_category(name)
Crea una nueva categoría

```python
create_category("Libros")
```

#### update_category(category_id, name)
Actualiza una categoría

```python
update_category(1, "Electrónica Premium")
```

#### delete_category(category_id)
Elimina una categoría

```python
delete_category(1)
```

### Funciones de Productos

#### get_all_products()
Obtiene todos los productos con información de categoría

```python
products = get_all_products()
# Retorna: [(1, 'Laptop', 'Desc', 'Electrónica', 999.99, 5, 'path.jpg'), ...]
```

#### create_product(name, description, category_id, price, stock=0, image_path=None)
Crea un nuevo producto

```python
create_product("Laptop", "Gaming", 1, 999.99, 10, "img/laptop.jpg")
```

#### update_product(product_id, name, description, category_id, price, stock, image_path)
Actualiza un producto

```python
update_product(1, "Laptop Pro", "Gaming Pro", 1, 1299.99, 5, "img/laptop_pro.jpg")
```

#### delete_product(product_id)
Elimina un producto

```python
delete_product(1)
```

#### get_product_by_id(product_id)
Obtiene un producto específico

```python
product = get_product_by_id(1)
```

### Funciones de Movimientos

#### register_movement(product_id, movement_type, quantity, description="")
Registra un movimiento y actualiza stock

```python
register_movement(1, "entrada", 10, "Compra a proveedor")
# Actualiza: products.stock += 10

register_movement(1, "salida", 2, "Venta cliente")
# Actualiza: products.stock -= 2
```

#### get_all_movements()
Obtiene el historial de movimientos

```python
movements = get_all_movements()
```

---

## Configuración

### Cambiar Servidor de Base de Datos

**Opción 1: Usar otra BD en Aiven**

1. Actualiza las credenciales en `DB_CONFIG`
2. Reinicia la aplicación

**Opción 2: Usar BD local**

```python
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'password',
    'database': 'inventario',
    'charset': 'utf8mb4'
}
```

### Cambiar Puerto de Conexión

Modifica `'port': 14788` en `DB_CONFIG`

### Cambiar Credenciales de Admin

Se generan automáticamente con las credenciales:
- Usuario: `admin`
- Contraseña: `admin`

Para cambiar, modifica `create_admin_user_if_not_exists()`

---

## Compilación del Ejecutable

### Requisitos
```powershell
pip install pyinstaller
```

### Método 1: Usando archivo .spec (Recomendado)

```powershell
cd C:\Users\[Usuario]\OneDrive\Documents\Python\Inventario
pyinstaller build.spec
```

### Método 2: Comando directo

```powershell
pyinstaller --onefile --windowed --icon=favicon.ico --name="Inventario" main.py
```

### Opciones de PyInstaller

| Opción | Descripción |
|--------|-------------|
| `--onefile` | Genera un único archivo ejecutable |
| `--windowed` | No muestra ventana de consola |
| `--icon=favicon.ico` | Establece icono de aplicación |
| `--name="Inventario"` | Nombre del ejecutable |
| `--console` | Muestra ventana de consola |

### Salida

El ejecutable se genera en:
```
Inventario/dist/Inventario.exe
```

### Crear Instalador (Opcional)

Usa NSIS o Inno Setup para crear un instalador profesional.

---

## Debugging

### Habilitar Modo Debug en VS Code

**Archivo:** `.vscode/launch.json`

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: main.py",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "console": "integratedTerminal",
            "justMyCode": true,
            "env": {"PYTHONPATH": "${workspaceFolder}"}
        }
    ]
}
```

### Puntos de Quiebre (Breakpoints)

1. Haz clic en el margen izquierdo de una línea
2. Presiona F5 para iniciar debug
3. Usa F10 (Step Over) o F11 (Step Into)

### Logs y Mensajes

```python
print("DEBUG: valor =", variable)
import logging
logging.debug("Información de debug")
```

### Cambiar Versión de Python

1. Presiona `Ctrl + Shift + P`
2. Escribe "Python: Select Interpreter"
3. Elige la versión deseada

---

## Seguridad

### Autenticación

- Las contraseñas se almacenan hasheadas con SHA256
- No se guardan contraseñas en texto plano
- Validación en el servidor (lado de la BD)

### Transmisión de Datos

- Usa SSL/TLS para conexiones (certificado ca.pem)
- Datos encriptados en tránsito
- Puerto seguro: 14788

### Credenciales en Código

⚠️ **IMPORTANTE:** Las credenciales están en el código por demostración.

**Para producción:**
```python
import os
DB_CONFIG = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    ...
}
```

### Validación de Entrada

Todas las funciones validan:
- Campos obligatorios
- Tipos de datos correctos
- Formatos válidos

---

## Mantenimiento

### Tareas Regulares

#### Diarias
- Verificar logs de errores
- Confirmar conectividad a BD

#### Semanales
- Respaldar base de datos
- Revisar rendimiento

#### Mensuales
- Limpieza de datos antiguos
- Actualizar dependencias

```powershell
pip list --outdated
pip install --upgrade [nombre-paquete]
```

### Respaldo de Base de Datos

```bash
mysqldump -h [host] -u [usuario] -p [base_datos] > respaldo.sql
```

### Restaurar Base de Datos

```bash
mysql -h [host] -u [usuario] -p [base_datos] < respaldo.sql
```

### Monitoreo

Revisa logs en:
- `~AppData\Local\[Aplicación]\logs` (Windows)
- Console output de la aplicación

### Actualización de Dependencias

```powershell
pip install --upgrade -r requirements.txt
```

---

## Troubleshooting Técnico

### Error: "ModuleNotFoundError: No module named 'PySide6'"

```powershell
pip install PySide6
```

### Error: "Connection refused" (Base de datos)

1. Verifica conexión a Internet
2. Comprueba credenciales en DB_CONFIG
3. Verifica que el servidor Aiven esté operativo

### Error: "SSL certificate problem"

1. Asegúrate que `ca.pem` existe en la carpeta
2. Verifica permisos de lectura

### Aplicación lenta

1. Verifica conexión a Internet
2. Revisa carga de la BD
3. Optimiza queries

### Memory leak

```python
import tracemalloc
tracemalloc.start()
# ... código ...
current, peak = tracemalloc.get_traced_memory()
print(f"Actual: {current / 1024}KB; Pico: {peak / 1024}KB")
```

---

## Soporte y Referencias

### Documentación Oficial
- [PySide6 Documentation](https://doc.qt.io/qtforpython/)
- [PyMySQL Documentation](https://pymysql.readthedocs.io/)
- [PyInstaller Documentation](https://pyinstaller.org/)

### Recursos Útiles
- [Aiven Documentation](https://aiven.io/docs/)
- [MySQL Tutorial](https://dev.mysql.com/doc/mysql-tutorial-excerpt/5.7/en/)
- [Python Security](https://python.readthedocs.io/en/latest/library/security_warnings.html)

---

**Versión:** 1.0
**Última actualización:** Febrero 2026
**Desarrollador:** Sistema de Inventario
**Soporte técnico:** contacto@inventario.local
