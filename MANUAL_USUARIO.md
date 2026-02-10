# 📚 Manual de Usuario - Sistema de Inventario

**Versión:** 2.0  
**Última actualización:** Febrero 2026  
**Aplicación:** Sistema de Gestión de Inventario Profesional

---

## 📋 Índice
1. [Proposito](#proposito)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación Paso a Paso](#instalación-paso-a-paso)
4. [Inicio de Sesión](#inicio-de-sesión)
5. [Interfaz Principal](#interfaz-principal)
6. [Gestión de Productos](#gestión-de-productos)
7. [Gestión de Categorías](#gestión-de-categorías)
8. [Registro de Movimientos](#registro-de-movimientos)
9. [Consejos y Mejores Prácticas](#consejos-y-mejores-prácticas)
10. [Solución de Problemas](#solución-de-problemas)
11. [Preguntas Frecuentes](#preguntas-frecuentes)
12. [Contáctenos](#contáctenos)

---

## Proposito

El **Sistema de Inventario** es una aplicación profesional de escritorio diseñada para gestionar de forma eficiente y segura:
- ✅ Catálogo completo de productos
- ✅ Categorización inteligente
- ✅ Control de movimientos de stock
- ✅ Historial detallado de operaciones
- ✅ Interfaz moderna e intuitiva
- ✅ Base de datos segura en la nube
- ✅ Autenticación por usuario
- ✅ Validaciones de datos avanzadas

**¿A quién va dirigido?**
- Pequeños y medianos negocios
- Tiendas al por menor
- Almacenes
- Distribuidoras
- Cualquier negocio que necesite controlar inventario

---

## Requisitos del Sistema

### 🖥️ Requisitos Mínimos
- **Sistema Operativo:** Windows 7 o superior (64 bits)
- **Memoria RAM:** 2 GB
- **Espacio en Disco:** 200 MB libres
- **Conexión:** Internet (broadband recomendado)
- **Pantalla:** Resolución mínima 1024x768

### ⭐ Requisitos Recomendados
- **Sistema Operativo:** Windows 10 o 11 (64 bits)
- **Memoria RAM:** 4 GB o superior
- **Procesador:** Intel i5 o equivalente
- **Conexión:** Fibra óptica o banda ancha estable
- **Pantalla:** 1920x1080 (Full HD) o superior

### 🔌 Conectividad
- Conexión a Internet **permanente** (aplicación en la nube)
- Velocidad mínima: 1 Mbps
- Latencia recomendada: < 100ms

---

## Instalación Paso a Paso

### 🚀 Opción 1: Usar el Ejecutable (RECOMENDADO - Más Fácil)

**Ventajas:**
- ✅ No requiere Python
- ✅ Instalación en segundos
- ✅ No necesita configuración
- ✅ Perfecto para usuarios no técnicos

**Pasos:**

1. **Descarga el archivo**
   - Busca el archivo `Inventario.exe` en tu correo o carpeta de descargas
   - Tamaño: ~150 MB
   - Arquitectura: Windows 64 bits

2. **Instala la aplicación**
   ```
   1. Haz doble clic en "Inventario.exe"
   2. Se abrirá una ventana (no instala nada, es portable)
   3. ¡Listo! La aplicación está lista para usar
   ```

3. **Acceso rápido (Opcional)**
   - Crea un acceso directo en el escritorio
   - Clic derecho en el .exe → Enviar a → Escritorio

4. **Primer uso**
   - La aplicación creará automáticamente las tablas necesarias
   - Espera 5-10 segundos en la primera ejecución
   - Verás un mensaje de confirmación

### 💻 Opción 2: Instalar desde Código Fuente (Para Desarrolladores)

**Requisitos previos:**
- Python 3.9 o superior ([Descargar aquí](https://www.python.org/downloads/))
- Terminal/PowerShell
- Acceso a Internet

**Pasos detallados:**

1. **Descarga el código fuente**
   ```powershell
   # Opción A: Si tienes Git
   git clone https://github.com/[usuario]/inventario.git
   cd inventario
   
   # Opción B: Manual
   # 1. Descarga el ZIP del proyecto
   # 2. Descomprímelo en tu carpeta deseada
   # 3. Abre PowerShell en esa carpeta
   ```

2. **Crea un entorno virtual (Recomendado)**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Instala las dependencias**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Ejecuta la aplicación**
   ```powershell
   python main.py
   ```

5. **Crear ejecutable personalizado (Opcional)**
   ```powershell
   pyinstaller --onefile --windowed --icon=favicon.ico main.py
   # El ejecutable estará en: dist/main.exe
   ```

---

## Inicio de Sesión

### 🔐 Pantalla de Login

La pantalla de login es tu primera línea de defensa. Solo usuarios autorizados pueden acceder.

### Credenciales por Defecto

**Para primera vez:**
```
Usuario: admin
Contraseña: admin
```

⚠️ **IMPORTANTE:** Cambia estas credenciales inmediatamente después del primer acceso.

### Cómo Iniciar Sesión

**Paso 1:** Abre la aplicación
- Haz doble clic en `Inventario.exe`
- O ejecuta `python main.py`

**Paso 2:** Completa los campos
```
┌─────────────────────────────────┐
│   Sistema de Inventario         │
├─────────────────────────────────┤
│                                 │
│  Usuario:    [______________]   │
│  Contraseña: [______________]   │
│                                 │
│  [Iniciar Sesión]               │
└─────────────────────────────────┘
```

**Paso 3:** Valida tu identidad
- Ingresa tu usuario (sensible a mayúsculas)
- Ingresa tu contraseña (sensible a mayúsculas)
- Haz clic en "Iniciar Sesión"

### ✅ Inicio Exitoso
- Verás el menú principal
- Aparecerá un saludo personalizado
- La hora de acceso se registrará

### ❌ Error de Acceso

**Mensaje:** "Credenciales incorrectas"

**Causas comunes:**
1. ✗ Usuario escrito mal
2. ✗ Contraseña incorrecta
3. ✗ Bloq Mayús activado
4. ✗ Espacios en blanco extra

**Soluciones:**
```
1. Verifica que escribes correctamente (sin espacios al inicio/final)
2. Comprueba si Bloq Mayús está activado
3. Respeta mayúsculas y minúsculas
4. Si olvidaste la contraseña, contacta al administrador
```

### 🔒 Consejos de Seguridad

| ✓ Buenas Prácticas | ✗ Evita |
|-------------------|---------|
| Contraseña única y fuerte | Compartir credenciales |
| Cambio regular de contraseña | Guardar contraseña en papel |
| Cierre de sesión al terminar | Dejar sesión abierta |
| Contraseñas sin datos personales | Contraseñas obvias (123456, admin) |

---

## Interfaz Principal

### 📊 Descripción General

Una vez autenticado, accederás a la interfaz principal dividida en **3 secciones principales:**

```
┌──────────────────────────────────────────────────────────┐
│  Sistema de Inventario                        [Cerrar]   │
├──────────────────────────────────────────────────────────┤
│  [Productos] [Categorías] [Movimientos]                  │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  Formulario de entrada + Tabla de datos                 │
│                                                          │
├──────────────────────────────────────────────────────────┤
│  [Cerrar Sesión]                                        │
└──────────────────────────────────────────────────────────┘
```

### 🔑 Elementos Principales

#### Barra de Pestañas
- **Productos:** Gestión del catálogo
- **Categorías:** Organización de items
- **Movimientos:** Historial de transacciones

#### Área de Formularios
- Campos para ingreso de datos
- Validación en tiempo real
- Botones de acción contextuales

#### Tabla de Datos
- Visualización de registros
- Selección para editar/eliminar
- Ordenamiento automático

#### Barra de Acciones
- Botones de Cerrar Sesión
- Botones de Ayuda (próximamente)
- Estado de conexión

---

## Gestión de Productos

### 📦 Información General

Los productos son los artículos que vende tu negocio. Cada producto contiene:
- Identificador único (ID)
- Nombre descriptivo
- Descripción detallada
- Categoría asignada
- Precio unitario
- Cantidad en stock
- Ruta de imagen (opcional)

### ➕ Agregar un Producto

**Pasos:**

1. **Dirígete a la pestaña "Productos"**

2. **Completa los campos:**
   
   | Campo | Tipo | Obligatorio | Ejemplo |
   |-------|------|------------|---------|
   | Nombre | Texto | ✓ Sí | "Laptop HP 15" |
   | Descripción | Texto largo | ✗ No | "Intel i7, 16GB RAM, SSD 512GB" |
   | Categoría | Selección | ✓ Sí | "Electrónica" |
   | Precio | Número decimal | ✓ Sí | "1299.99" |
   | Stock | Número entero | ✓ Sí | "50" |
   | Imagen | Ruta | ✗ No | "C:\imagenes\laptop.jpg" |

3. **Valida los datos:**
   - ✓ El nombre no está vacío
   - ✓ Seleccionaste una categoría
   - ✓ El precio es mayor a 0
   - ✓ El stock es numérico

4. **Haz clic en "Agregar Producto"**

5. **Confirma el éxito:**
   - Verás un mensaje: "Producto agregado correctamente"
   - El producto aparecerá en la tabla
   - El formulario se limpiará

### 🔍 Búsqueda y Visualización

La tabla inferior muestra **todos tus productos** con:

| Columna | Contenido |
|---------|-----------|
| ID | Identificador único (autogenerado) |
| Nombre | Nombre del producto |
| Descripción | Detalles y características |
| Categoría | Familia del producto |
| Precio | Precio unitario |
| Stock | Unidades disponibles |
| Imagen | Ruta del archivo |

**Características de la tabla:**
- ✓ Scroll automático si hay muchos productos
- ✓ Ancho adaptable de columnas
- ✓ Búsqueda por clic en fila
- ✓ Selección múltiple (próximamente)

### ✏️ Editar un Producto

**Procedimiento:**

1. **Selecciona el producto**
   - Haz clic en cualquier celda de la fila
   - La fila se resaltará en azul
   - Los datos se cargarán en el formulario

2. **Modifica los datos que desees**
   ```
   Antes: "Laptop HP 15" → Precio: $1299.99
   Después: "Laptop HP 15 PRO" → Precio: $1599.99
   ```

3. **Haz clic en "Actualizar Seleccionado"**

4. **Confirma los cambios**
   - Verás: "Producto actualizado correctamente"
   - La tabla se refrescará automáticamente
   - El stock se mantendrá

### 🗑️ Eliminar un Producto

**ADVERTENCIA:** Esta acción es **permanente e irreversible**

**Procedimiento:**

1. **Selecciona el producto a eliminar**
   - Clic en la fila del producto

2. **Haz clic en "Eliminar Seleccionado"**

3. **Confirma la acción**
   ```
   ┌────────────────────────────────────┐
   │ ⚠️ Confirmar                        │
   │                                    │
   │ ¿Estás seguro de que deseas       │
   │ eliminar este producto?            │
   │                                    │
   │ [Sí, eliminar] [Cancelar]         │
   └────────────────────────────────────┘
   ```

4. **Resultado**
   - El producto se elimina de la BD
   - Ya no aparecerá en la tabla
   - El ID nunca se reutilizará

### 🔄 Limpiar Formulario

Haz clic en **"Limpiar"** para:
- Vaciar todos los campos
- Deseleccionar categoría
- Resetear valores numéricos
- Permitir ingresar un nuevo producto

### 💡 Mejores Prácticas

| ✓ Recomendado | ✗ Evitar |
|---------------|----------|
| Nombres descriptivos | Nombres genéricos como "producto" |
| Precios precisos | Precios redondeados incorrectamente |
| Stock actualizado | Información desactualizada |
| Categoría correcta | Producto sin categoría |
| Descripciones detalladas | Descripción vacía |
| Revisión antes de guardar | Datos sin verificar |

---

## Gestión de Categorías

Las categorías organizan lógicamente tus productos, facilitando búsqueda y análisis.

### 📑 ¿Por qué usar categorías?

**Beneficios:**
- ✓ Organización clara del catálogo
- ✓ Búsqueda más rápida
- ✓ Reportes y análisis por categoría
- ✓ Control de inventario por familia
- ✓ Facilita gestión de proveedores

### 📋 Ejemplo de Categorías

```
Categoría: Electrónica
├── Computadoras
├── Periféricos
└── Accesorios

Categoría: Ropa
├── Camisetas
├── Pantalones
└── Accesorios

Categoría: Hogar
├── Cocina
├── Baño
└── Sala
```

### ➕ Crear una Categoría

**Pasos:**

1. **Abre la pestaña "Categorías"**

2. **Ingresa el nombre**
   ```
   Campo: Nombre de la Categoría
   Ejemplo: "Electrónica", "Ropa", "Alimentos"
   ```

3. **Características del nombre:**
   - Máximo 100 caracteres
   - No pueden repetirse
   - Sin caracteres especiales (ñ, acentos sí)
   - Claridad y simplicidad

4. **Haz clic en "Agregar Categoría"**

5. **Confirmación**
   - Aparecerá el mensaje: "Categoría agregada correctamente"
   - La categoría se mostrará en la tabla
   - Estará disponible al crear productos

### ✏️ Editar una Categoría

**Procedimiento:**

1. **Selecciona la categoría**
   - Clic en la fila en la tabla

2. **El nombre aparecerá en el formulario**

3. **Modifica el nombre**
   - Borrar el anterior
   - Escribir el nuevo nombre

4. **Haz clic en "Actualizar Seleccionada"**

5. **Verificación:**
   - Mensaje de éxito
   - Los productos mantienen su asociación
   - La tabla se actualiza

### 🗑️ Eliminar una Categoría

**IMPORTANTE:** No puedes eliminar una categoría si tiene productos asociados.

**Procedimiento:**

1. **Verifica que la categoría está vacía**
   - En la pestaña Productos, cambia los productos de categoría si es necesario

2. **Selecciona la categoría**

3. **Haz clic en "Eliminar Seleccionada"**

4. **Confirma la acción**
   - Si hay productos: "No puedes eliminar una categoría con productos"
   - Si está vacía: "Categoría eliminada correctamente"

### 🏷️ Categorías Recomendadas

Para diferentes tipos de negocio:

**Tienda de Ropa:**
```
- Camisetas
- Pantalones
- Vestidos
- Accesorios
- Calzado
```

**Tienda de Electrónica:**
```
- Computadoras
- Smartphones
- Accesorios
- Periféricos
- Componentes
```

**Almacén de Alimentos:**
```
- Lácteos
- Carnes
- Frutas y Verduras
- Bebidas
- Granos y Cereales
```

**Farmacia:**
```
- Medicamentos
- Vitaminas
- Higiene Personal
- Primeros Auxilios
- Suplementos
```

---

## Registro de Movimientos

### 📊 ¿Qué son los movimientos?

Los movimientos registran **todas las transacciones** de stock:
- Entradas: productos que llegan al almacén
- Salidas: productos que salen del almacén

Cada movimiento queda **documentado con:**
- Producto involucrado
- Tipo de movimiento
- Cantidad
- Fecha y hora
- Descripción/motivo

### 📈 Tipos de Movimientos

#### ENTRADA (Incrementa el Stock)
**Casos de uso:**
- Compra a proveedores
- Devoluciones de clientes
- Ajuste de inventario
- Recepción de transferencia
- Reparación/devolución de cliente

```
Ejemplo:
- Compré 100 unidades de productos
- Acción: Movimiento → ENTRADA → Cantidad: 100
- Stock anterior: 50 → Stock nuevo: 150
```

#### SALIDA (Reduce el Stock)
**Casos de uso:**
- Venta a clientes
- Pérdida/daño
- Devolución a proveedor
- Transferencia entre almacenes
- Muestrario

```
Ejemplo:
- Vendí 5 productos
- Acción: Movimiento → SALIDA → Cantidad: 5
- Stock anterior: 150 → Stock nuevo: 145
```

### ➕ Registrar un Movimiento

**Procedimiento paso a paso:**

1. **Abre la pestaña "Movimientos"**

2. **Selecciona el producto**
   - Dropdown: "Producto"
   - Solo muestra productos existentes
   - Ejemplo: "Laptop HP 15"

3. **Elige el tipo de movimiento**
   - **Entrada:** Stock aumenta
   - **Salida:** Stock disminuye

4. **Ingresa la cantidad**
   - Número positivo
   - No puede ser 0
   - Máximo 999,999 unidades

5. **Descripción (Opcional)**
   - Motivo del movimiento
   - Ejemplo: "Venta cliente 001"
   - Facilita auditoría posterior

6. **Verifica los datos**
   ```
   Producto: Laptop HP 15
   Tipo: Entrada
   Cantidad: 50
   Descripción: Compra a proveedor ABC
   ```

7. **Haz clic en "Registrar Movimiento"**

8. **Confirmación:**
   - Verás: "Movimiento registrado correctamente"
   - Stock del producto se actualiza
   - Tabla de movimientos se refresca
   - Historial se documenta

### 📋 Historial de Movimientos

La tabla muestra **todos los movimientos registrados:**

| Columna | Información |
|---------|------------|
| ID | Número de movimiento único |
| Producto | Nombre del producto afectado |
| Tipo | Entrada o Salida |
| Cantidad | Unidades movidas |
| Fecha | Fecha y hora exacta |
| Descripción | Motivo del movimiento |

**Características:**
- Ordenado por fecha (más recientes primero)
- No se pueden eliminar movimientos
- Se guardan permanentemente
- Sirven para auditoría

### 🔍 Ejemplos Prácticos

#### Ejemplo 1: Compra a Proveedor
```
Producto: Camisetas Negras
Tipo: ENTRADA
Cantidad: 100
Descripción: Compra a TextilExpo - Factura #5432
Resultado: Stock +100
```

#### Ejemplo 2: Venta a Cliente
```
Producto: Camisetas Negras
Tipo: SALIDA
Cantidad: 5
Descripción: Venta cliente Juan López
Resultado: Stock -5
```

#### Ejemplo 3: Ajuste por Pérdida
```
Producto: Camisetas Negras
Tipo: SALIDA
Cantidad: 2
Descripción: Pérdida por daño en almacén
Resultado: Stock -2
```

#### Ejemplo 4: Devolución de Cliente
```
Producto: Camisetas Negras
Tipo: ENTRADA
Cantidad: 1
Descripción: Devolución cliente - talla incorrecta
Resultado: Stock +1
```

### ⚠️ Errores Comunes

| Error | Solución |
|-------|----------|
| "Producto no seleccionado" | Elige un producto del dropdown |
| "Cantidad inválida" | Ingresa un número positivo y válido |
| "Tipo no seleccionado" | Elige ENTRADA o SALIDA |
| Stock negativo después | Verifica cantidad antes de registrar |

### 💡 Mejores Prácticas

✓ **DO's:**
- Registra movimientos al mismo momento de la transacción
- Sé descriptivo en las notas
- Verifica cantidades antes de confirmar
- Revisa el historial regularmente
- Mantén movimientos con categorías claras

✗ **DON'Ts:**
- No registres movimientos incorrectos (es permanente)
- No confundas entrada/salida
- No dejes descripciones vacías
- No registres con cantidades aproximadas
- No ignores el historial de auditoría

---

## Solución de Problemas (Guía Completa)

### 🔴 Problema: La aplicación no inicia

**Síntoma:** Hago doble clic en Inventario.exe pero no pasa nada

**Causas posibles:**
1. Archivo corrupto
2. Permisos insuficientes
3. Antivirus bloqueando
4. Falta de dependencias (versión código fuente)

**Soluciones:**

✓ **Intenta 1:** Ejecutar como administrador
```
1. Clic derecho en Inventario.exe
2. "Ejecutar como administrador"
3. Confirma el cuadro de diálogo
```

✓ **Intenta 2:** Revisar antivirus
```
1. Abre tu antivirus
2. Busca "Inventario" en la cuarentena
3. Restaura o crea una excepción
4. Reinicia la aplicación
```

✓ **Intenta 3:** Descargar nuevamente
```
1. Elimina el archivo corrupto
2. Descarga una copia fresca
3. Coloca en carpeta sin caracteres especiales
4. Ejecuta
```

✓ **Intenta 4:** Si nada funciona
- Contacta a soporte técnico
- Proporciona: versión SO, antivirus, modo de instalación

---

### 🔴 Problema: Error de conexión a BD

**Síntoma:** "Error al conectar con la base de datos"

**Causas comunes:**
1. ❌ Sin conexión a Internet
2. ❌ Servidor Aiven inactivo
3. ❌ Credenciales incorrectas
4. ❌ Firewall bloqueando

**Soluciones:**

✓ **Paso 1:** Verifica Internet
```
Prueba:
- Abre navegador
- Intenta acceder a Google.com
- Si funciona, continúa

Si no funciona:
- Reinicia el módem/router
- Contacta a ISP
```

✓ **Paso 2:** Verifica servidor
```
Estado del servidor:
- Aiven Dashboard online
- Servidor en estado "Running"
- Certificado SSL válido
```

✓ **Paso 3:** Prueba la conexión
```
PowerShell/CMD:
ping inventario-ortizcruzbrian-0474.c.aivencloud.com
```

✓ **Paso 4:** Reinicia la aplicación
```
1. Cierra completamente Inventario
2. Espera 5 segundos
3. Reabre la aplicación
4. Intenta login
```

---

### 🔴 Problema: No puedo iniciar sesión

**Síntoma:** "Credenciales incorrectas" pero sé que están bien

**Causas:**
1. ❌ Bloq Mayús activado
2. ❌ Espacios en blanco extra
3. ❌ Usuario no existe
4. ❌ Contraseña olvidada

**Soluciones:**

✓ **Verifica Bloq Mayús**
```
- Presiona Bloq Mayús si está activado
- Prueba nuevamente
```

✓ **Sin espacios extra**
```
Usuario: "admin" ✓ (correcto)
Usuario: " admin " ✗ (espacios)
Usuario: "Admin" ✗ (mayúscula diferente)
```

✓ **Reinicia la aplicación**
```
Cierra y reabre para resetear estado
```

✓ **Contraseña olvidada**
```
Contacta al administrador:
- Requiere reset manual
- No hay recuperación automática
```

---

### 🔴 Problema: Tabla vacía

**Síntoma:** Pestaña Productos/Categorías muestra tabla vacía

**Causas:**
1. ❌ Base de datos vacía (primera vez)
2. ❌ Datos no cargados
3. ❌ Error de conexión

**Soluciones:**

✓ **Opción 1:** Cambiar de pestaña y volver
```
1. Haz clic en otra pestaña
2. Vuelve a la pestaña original
3. Datos deberían cargar
```

✓ **Opción 2:** Agregar datos
```
Si es primera vez:
1. Crea una categoría primero
2. Luego crea un producto
3. Verás datos en la tabla
```

✓ **Opción 3:** Refrescar la aplicación
```
1. Cierra la aplicación
2. Abre nuevamente
3. Navega a la pestaña
```

---

### 🔴 Problema: No puedo editar/eliminar

**Síntoma:** Los botones de editar/eliminar no funcionan

**Causa:** No has seleccionado un registro

**Solución:**
```
1. Haz clic en la fila de la tabla
2. La fila se resaltará
3. Ahora sí puedes editar/eliminar
```

---

### 🔴 Problema: Mensaje "Nombre es obligatorio"

**Síntoma:** Al agregar producto: "El nombre es obligatorio"

**Soluciones:**
```
1. Verifica que el campo Nombre NO está vacío
2. Completa todos los campos requeridos (*)
3. Evita solo espacios en blanco
```

---

### 🔴 Problema: Categoría no aparece en dropdown

**Síntoma:** Creé categoría pero no aparece al agregar producto

**Solución:**
```
1. Recarga la aplicación
2. Las categorías deberían aparecer
3. Si aún no, verifica:
   - Categoría creada correctamente
   - Permiso de lectura en BD
```

---

### 🔴 Problema: Stock negativo

**Síntoma:** Stock quedó negativo después de venta

**Causa:** Registraste una SALIDA mayor que el stock

**Solución:**
```
1. Registra una ENTRADA para corregir
2. Ejemplo: si Stock es -5
3. Registra ENTRADA de 5 unidades
4. Stock vuelve a 0
```

---

### 🔴 Problema: Aplicación lenta

**Síntoma:** Responde lentamente, especialmente al cargar tablas

**Causas:**
1. ❌ Conexión lenta
2. ❌ Muchos datos
3. ❌ Servidor lento

**Soluciones:**

✓ **Mejora tu conexión**
```
- Muévete más cerca del router
- Usa cable en lugar de WiFi
- Cierra otras aplicaciones
```

✓ **Reduce cantidad de datos**
```
- Los registros muy antiguos se pueden archivar
- Consulta al administrador
```

✓ **Intenta en otra hora**
```
- El servidor podría estar ocupado
- Servidor se mantiene 2-4 AM
```

---

### 🆘 Problema: Error no listado aquí

**Si el problema persiste:**

1. **Toma nota de:**
   - Mensaje de error exacto
   - Qué estabas haciendo
   - Tu sistema operativo
   - Tipo de conexión

2. **Contacta a soporte:**
   - Email: soporte@inventario.local
   - Teléfono: +34 XXX XXX XXX
   - Proporciona la información anterior

---

## Consejos y Mejores Prácticas

### 🎯 Para Usuarios Principiantes

**Primera vez:**
1. Crea 3-5 categorías básicas
2. Agrega 10 productos de ejemplo
3. Practica movimientos
4. Revisa el historial

**Seguridad:**
1. Cambia la contraseña inicial
2. Cierra sesión siempre
3. No compartas credenciales
4. Usa contraseña única y fuerte

**Efectividad:**
1. Crea categorías significativas
2. Usa descripciones claras
3. Registra movimientos inmediatamente
4. Revisa reportes regularmente

### 💼 Para Usuarios Avanzados

**Optimización:**
```
- Usa búsqueda por categoría
- Revisa movimientos diarios
- Mantén stock > umbral mínimo
- Realiza auditoría mensual
```

**Datos:**
```
- Realiza backup de datos
- Documenta procedimientos
- Capacita a equipo
- Usa reportes para decisiones
```

**Seguridad:**
```
- Rota contraseñas mensualmente
- Revisa accesos
- Audita cambios
- Reporta anomalías
```

---

## Preguntas Frecuentes

### ¿Puedo usar la aplicación sin Internet?

No, la aplicación requiere conexión a Internet porque los datos se almacenan en una base de datos en la nube.

### ¿Cuántos usuarios puedo crear?

Puedes crear múltiples usuarios. Contacta al administrador para agregar nuevos usuarios con diferentes roles (admin/employee).

### ¿Puedo recuperar un producto eliminado?

No, la eliminación es permanente. Ten cuidado al eliminar datos.

### ¿Cómo cambio mi contraseña?

Actualmente, las contraseñas se gestionan a nivel de administrador. Contacta al administrador del sistema.

### ¿Puedo exportar los datos?

Actualmente no hay función de exportación. Esta característica se puede agregar en futuras versiones.

### ¿Es segura mi información?

Sí, todos los datos se transmiten de forma segura (SSL/TLS) y se almacenan en servidores seguros.

### ¿Qué pasa si pierdo mi conexión a Internet durante una operación?

Las operaciones se completan en el servidor. Si pierdes conexión, intenta de nuevo cuando recuperes la conexión.

### ¿Puedo usar la aplicación en Mac o Linux?

Sí, instalando desde código fuente con Python. El ejecutable .exe solo funciona en Windows.

---

## Contacto y Soporte

Para más ayuda o reportar problemas:
- Contacta al administrador del sistema
- Verifica la documentación técnica (MANUAL_TECNICO.md)

---

**Versión:** 1.0
**Última actualización:** Febrero 2026
**Desarrollador:** Sistema de Inventario
