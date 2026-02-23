# 🛍️ Tienda de Ropa - Base de Datos MongoDB

Base de datos no relacional para una tienda de ropa, implementada en **MongoDB Atlas**. Incluye operaciones CRUD completas y consultas de análisis de ventas.

---

## 📁 Estructura del Repositorio

```
tienda-ropa-mongodb/
│
├── database/
│   └── tiendaRopa.js   # Script principal con BD, colecciones y consultas
└── README.md           # Documentación del proyecto
```

---

## 🗄️ Colecciones

El diseño sigue el enfoque **no relacional**: los datos relacionados se **embeben** dentro del documento en lugar de referenciar otras colecciones, lo que reduce los *joins* y mejora el rendimiento en lecturas.

### 1. `usuarios`
Almacena los datos de los clientes registrados en la tienda.

| Campo           | Tipo   | Descripción                     |
|-----------------|--------|---------------------------------|
| `nombre`        | String | Nombre completo del usuario     |
| `email`         | String | Correo electrónico              |
| `telefono`      | String | Número de contacto              |
| `direccion`     | String | Ubicación del usuario           |
| `fechaRegistro` | Date   | Fecha de registro en el sistema |

**Ejemplo de documento:**
```json
{
  "nombre": "Gael Montiel",
  "email": "gael.montiel@gmail.com",
  "telefono": "8745-2190",
  "direccion": "Cartago",
  "fechaRegistro": "2025-02-22"
}
```

---

### 2. `marcas`
Almacena la información de las marcas de ropa disponibles.

| Campo        | Tipo   | Descripción                 |
|--------------|--------|-----------------------------|
| `nombre`     | String | Nombre de la marca          |
| `paisOrigen` | String | País de origen de la marca  |
| `categoria`  | String | Tipo de moda que representa |

**Ejemplo de documento:**
```json
{
  "nombre": "Aurelia Studio",
  "paisOrigen": "Italia",
  "categoria": "Moda contemporánea"
}
```

---

### 3. `prendas`
Almacena las prendas disponibles en la tienda con sus detalles.

| Campo    | Tipo   | Descripción                       |
|----------|--------|-----------------------------------|
| `nombre` | String | Nombre de la prenda               |
| `marca`  | String | Marca a la que pertenece          |
| `talla`  | String | Talla disponible                  |
| `precio` | Number | Precio en colones                 |
| `stock`  | Number | Cantidad disponible en inventario |

**Ejemplo de documento:**
```json
{
  "nombre": "Blazer Oversize Lino",
  "marca": "Aurelia Studio",
  "talla": "M",
  "precio": 42000,
  "stock": 12
}
```

---

### 4. `ventas`
Almacena cada transacción. Sigue el modelo **desnormalizado**: los datos del usuario y las prendas se guardan directamente en el documento.

| Campo    | Tipo   | Descripción                              |
|----------|--------|------------------------------------------|
| `usuario`| String | Nombre del cliente que realizó la compra |
| `prendas`| Array  | Lista de prendas compradas con cantidad  |
| `total`  | Number | Monto total de la compra                 |
| `fecha`  | Date   | Fecha de la transacción                  |

**Ejemplo de documento:**
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

---

## ⚙️ Operaciones CRUD

Cada colección incluye las siguientes operaciones:

| Operación        | Método MongoDB                  |
|------------------|---------------------------------|
| Insertar un dato | `insertOne()`                   |
| Insertar varios  | `insertMany()`                  |
| Actualizar       | `updateOne()`                   |
| Eliminar         | `deleteOne()` / `deleteMany()`  |

---

## 🔍 Consultas

| # | Descripción |
|---|-------------|
| 1 | Cantidad total de prendas vendidas agrupadas **por fecha** |
| 2 | Cantidad de prendas vendidas **filtrando por una fecha específica** |

---

## 🚀 Cómo ejecutar

1. Conectarse a **MongoDB Atlas** desde la terminal:
   ```bash
   mongosh "mongodb+srv://cluster0.xxxxx.mongodb.net/" --apiVersion 1 --username tuUsuario
   ```

2. Una vez conectado, cargar el archivo:
   ```js
   load("ruta/al/archivo/tiendaRopa.js")
   ```

3. Verificar las colecciones creadas:
   ```js
   use("tienda_ropa")
   show collections
   ```

---

## 🛠️ Tecnologías

- **MongoDB Atlas** — Base de datos NoSQL en la nube
- **GitHub** — Control de versiones
- **Markdown** — Documentación

---

## 👤 Autora

Proyecto desarrollado por **Melany Villarreal**.
