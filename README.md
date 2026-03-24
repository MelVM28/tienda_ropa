# 🛍️ Tienda de Ropa - Base de Datos & API REST

Proyecto completo de una tienda de ropa con base de datos **MongoDB Atlas** y una **API REST** desarrollada en **Python + Flask**.

---

## 📁 Estructura del Repositorio

```
tienda_ropa/
│
├── database/
│   └── tiendaRopa.js         # Script CRUD MongoDB (Parte I)
│
├── API/
│   └── v1/
│       ├── run.py             # Punto de entrada de la API
│       ├── requirements.txt   # Dependencias
│       └── app/
│           ├── __init__.py
│           ├── index.py       # Registro de rutas
│           ├── controllers/
│           │   ├── usuarios.py
│           │   ├── marcas.py
│           │   ├── prendas.py
│           │   ├── ventas.py
│           │   └── reportes.py
│           └── models/
│               ├── db.py
│               ├── usuario.py
│               ├── marca.py
│               ├── prenda.py
│               └── venta.py
│
└── README.md
```

---

## 🗄️ Parte I — Base de Datos MongoDB

El diseño sigue el enfoque **no relacional**: los datos relacionados se **embeben** dentro del documento en lugar de referenciar otras colecciones.

### Colecciones

### 1. `usuarios`
| Campo           | Tipo   | Descripción                     |
|-----------------|--------|---------------------------------|
| `nombre`        | String | Nombre completo del usuario     |
| `email`         | String | Correo electrónico              |
| `telefono`      | String | Número de contacto              |
| `direccion`     | String | Ubicación del usuario           |
| `fechaRegistro` | Date   | Fecha de registro en el sistema |

**Ejemplo:**
```json
{
  "nombre": "Gael Montiel",
  "email": "gael.montiel@gmail.com",
  "telefono": "8745-2190",
  "direccion": "Cartago",
  "fechaRegistro": "2025-02-22"
}
```

### 2. `marcas`
| Campo        | Tipo   | Descripción                 |
|--------------|--------|-----------------------------|
| `nombre`     | String | Nombre de la marca          |
| `paisOrigen` | String | País de origen de la marca  |
| `categoria`  | String | Tipo de moda que representa |

**Ejemplo:**
```json
{
  "nombre": "Aurelia Studio",
  "paisOrigen": "Italia",
  "categoria": "Moda contemporánea"
}
```

### 3. `prendas`
| Campo    | Tipo   | Descripción                       |
|----------|--------|-----------------------------------|
| `nombre` | String | Nombre de la prenda               |
| `marca`  | String | Marca a la que pertenece          |
| `talla`  | String | Talla disponible                  |
| `precio` | Number | Precio en colones                 |
| `stock`  | Number | Cantidad disponible en inventario |

**Ejemplo:**
```json
{
  "nombre": "Blazer Oversize Lino",
  "marca": "Aurelia Studio",
  "talla": "M",
  "precio": 42000,
  "stock": 12
}
```

### 4. `ventas`
| Campo     | Tipo   | Descripción                              |
|-----------|--------|------------------------------------------|
| `usuario` | String | Nombre del cliente que realizó la compra |
| `prendas` | Array  | Lista de prendas compradas con cantidad  |
| `total`   | Number | Monto total de la compra                 |
| `fecha`   | Date   | Fecha de la transacción                  |

**Ejemplo:**
```json
{
  "usuario": "Gael Montiel",
  "prendas": [{ "nombre": "Blazer Oversize Lino", "cantidad": 1 }],
  "total": 42000,
  "fecha": "2025-02-20"
}
```

### Operaciones CRUD
| Operación        | Método MongoDB                  |
|------------------|---------------------------------|
| Insertar un dato | `insertOne()`                   |
| Insertar varios  | `insertMany()`                  |
| Actualizar       | `updateOne()`                   |
| Eliminar         | `deleteOne()` / `deleteMany()`  |

### Consultas
| # | Descripción |
|---|-------------|
| 1 | Cantidad total de prendas vendidas agrupadas **por fecha** |
| 2 | Cantidad de prendas vendidas **filtrando por una fecha específica** |

### Cómo ejecutar el script
```bash
mongosh "mongodb+srv://cluster0.ux5x4h0.mongodb.net/" --apiVersion 1 --username mel_db
```
```js
load("ruta/al/archivo/tiendaRopa.js")
```

---

## 🚀 Parte II — API REST con Flask

### Cómo ejecutar la API
```bash
cd API/v1
pip install -r requirements.txt
python run.py
```
La API queda disponible en: `http://127.0.0.1:5000`

---

## 📡 Endpoints

### 👤 Usuarios

#### Obtener todos los usuarios
- **Método:** GET
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/usuarios`
- **Respuesta:**
```json
[
  {
    "_id": "65f3a2b1c4e5d6f7a8b9c0d1",
    "nombre": "Gael Montiel",
    "email": "gael.montiel@gmail.com",
    "telefono": "8745-2190",
    "direccion": "Cartago"
  }
]
```

#### Obtener usuario por ID
- **Método:** GET
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/usuarios/<id>`

#### Crear usuario
- **Método:** POST
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/usuarios`
- **Body:**
```json
{
  "nombre": "Gael Montiel",
  "email": "gael.montiel@gmail.com",
  "telefono": "8745-2190",
  "direccion": "Cartago",
  "fechaRegistro": "2025-02-22"
}
```

#### Actualizar usuario
- **Método:** PUT
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/usuarios/<id>`
- **Body:**
```json
{
  "telefono": "8888-9999"
}
```

#### Eliminar usuario
- **Método:** DELETE
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/usuarios/<id>`

---

### 🏷️ Marcas

#### Obtener todas las marcas
- **Método:** GET
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/marcas`

#### Obtener marca por ID
- **Método:** GET
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/marcas/<id>`

#### Crear marca
- **Método:** POST
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/marcas`
- **Body:**
```json
{
  "nombre": "Aurelia Studio",
  "paisOrigen": "Italia",
  "categoria": "Moda contemporánea"
}
```

#### Actualizar marca
- **Método:** PUT
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/marcas/<id>`
- **Body:**
```json
{
  "categoria": "Alta costura"
}
```

#### Eliminar marca
- **Método:** DELETE
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/marcas/<id>`

---

### 👗 Prendas

#### Obtener todas las prendas
- **Método:** GET
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/prendas`

#### Obtener prenda por ID
- **Método:** GET
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/prendas/<id>`

#### Crear prenda
- **Método:** POST
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/prendas`
- **Body:**
```json
{
  "nombre": "Blazer Oversize Lino",
  "marca": "Aurelia Studio",
  "talla": "M",
  "precio": 42000,
  "stock": 12
}
```

#### Actualizar prenda
- **Método:** PUT
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/prendas/<id>`
- **Body:**
```json
{
  "precio": 39000,
  "stock": 8
}
```

#### Eliminar prenda
- **Método:** DELETE
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/prendas/<id>`

---

### 🧾 Ventas

#### Obtener todas las ventas
- **Método:** GET
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/ventas`

#### Obtener venta por ID
- **Método:** GET
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/ventas/<id>`

#### Crear venta
- **Método:** POST
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/ventas`
- **Body:**
```json
{
  "usuario": "Gael Montiel",
  "prendas": [
    { "nombre": "Blazer Oversize Lino", "cantidad": 1 }
  ],
  "total": 42000,
  "fecha": "2025-02-20"
}
```

#### Actualizar venta
- **Método:** PUT
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/ventas/<id>`
- **Body:**
```json
{
  "total": 45000
}
```

#### Eliminar venta
- **Método:** DELETE
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/ventas/<id>`

---

### 📊 Reportes

#### Marcas con al menos una venta
- **Método:** GET
- **URL:** `http://127.0.0.1:5000/tienda/api/v1/reportes/marcas-con-ventas`
- **Respuesta:**
```json
[
  {
    "_id": "Aurelia Studio",
    "totalVentas": 3,
    "totalPrendas": 5
  }
]
```

---

## 🛠️ Tecnologías

- **Python + Flask** — API REST
- **PyMongo** — Conexión a MongoDB desde Python
- **MongoDB Atlas** — Base de datos NoSQL en la nube
- **GitHub** — Control de versiones
- **Postman** — Prueba de endpoints
- **Markdown** — Documentación

---

## 👤 Autora

Proyecto desarrollado por **Melany Villarreal**.
