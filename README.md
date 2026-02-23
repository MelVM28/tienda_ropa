# Base de Datos - Tienda de Ropa

## Descripción

Este proyecto consiste en la creación de una base de datos NoSQL utilizando MongoDB para una tienda de ropa.

La base de datos permite manejar información sobre:

- Usuarios
- Marcas
- Prendas
- Ventas

Se implementaron operaciones básicas como inserción, actualización, eliminación y consultas utilizando MongoDB.

---

## Tecnologías utilizadas

- MongoDB Atlas
- GitHub
- Markdown

---

## Estructura del repositorio

tienda-ropa-mongodb/
│
├── database/
│ └── tiendaRopa.js
│
└── README.md


---

## Ejemplos de documentos

### Usuario

```json
{
  "nombre": "Gael Montiel",
  "email": "gael.montiel@gmail.com",
  "telefono": "8745-2190",
  "direccion": "Cartago",
  "fechaRegistro": "2025-02-22"
}

{
  "nombre": "Aurelia Studio",
  "paisOrigen": "Italia",
  "categoria": "Moda contemporanea"
}

{
  "nombre": "Blazer Oversize Lino",
  "marca": "Aurelia Studio",
  "talla": "M",
  "precio": 42000,
  "stock": 12
}

{
  "usuario": "Gael Montiel",
  "prendas": [
    { "nombre": "Blazer Oversize Lino", "cantidad": 1 }
  ],
  "total": 42000,
  "fecha": "2025-02-20"
}
Consulta implementada

Se realizó una consulta utilizando aggregate() para obtener la cantidad total de prendas vendidas en una fecha específica.

Integrante:
Melany Villarreal

#V2
# 🛍️ Tienda de Ropa - Base de Datos MongoDB

Base de datos no relacional para una tienda de ropa, implementada en **MongoDB**. Incluye operaciones CRUD completas y consultas de análisis de ventas.

---

## 📁 Estructura del Repositorio

```
tienda-ropa-mongodb/
│
├── tienda_ropa.js   # Script principal con BD, colecciones y consultas
└── README.md        # Documentación del proyecto
```

---

## 🗄️ Colecciones

El diseño sigue el enfoque **no relacional**: los datos relacionados se **embeben** dentro del documento en lugar de referenciar otras colecciones, lo que reduce los *joins* y mejora el rendimiento en lecturas.

### 1. `productos`
Almacena las prendas disponibles. Cada producto incluye sus **variantes** (talla y color) como un array embebido.

| Campo         | Tipo     | Descripción                          |
|---------------|----------|--------------------------------------|
| `codigo`      | String   | Identificador único del producto     |
| `nombre`      | String   | Nombre de la prenda                  |
| `categoria`   | String   | Categoría (Camisetas, Pantalones…)   |
| `precio`      | Number   | Precio en USD                        |
| `variantes`   | Array    | Lista de { talla, color, stock }     |
| `activo`      | Boolean  | Indica si el producto está en venta  |
| `fechaIngreso`| Date     | Fecha de ingreso al catálogo         |

---

### 2. `clientes`
Almacena la información de los clientes registrados, incluyendo su dirección como **objeto embebido**.

| Campo           | Tipo     | Descripción                        |
|-----------------|----------|------------------------------------|
| `cedula`        | String   | Identificador único del cliente    |
| `nombre`        | String   | Nombre completo                    |
| `email`         | String   | Correo electrónico                 |
| `telefono`      | String   | Número de contacto                 |
| `direccion`     | Object   | { provincia, canton, detalle }     |
| `fechaRegistro` | Date     | Fecha de registro en el sistema    |
| `activo`        | Boolean  | Estado del cliente                 |

---

### 3. `ventas`
Almacena cada transacción de venta. Sigue el modelo **desnormalizado**: los datos del cliente y el detalle de cada prenda vendida se guardan directamente en el documento para evitar consultas adicionales.

| Campo          | Tipo     | Descripción                              |
|----------------|----------|------------------------------------------|
| `numeroFactura`| String   | Identificador único de la venta          |
| `fecha`        | Date     | Fecha de la transacción                  |
| `cliente`      | Object   | Datos del cliente al momento de la venta |
| `items`        | Array    | Lista de prendas vendidas con detalle    |
| `totalVenta`   | Number   | Monto total de la factura                |
| `metodoPago`   | String   | Tarjeta / Efectivo / Transferencia       |
| `estado`       | String   | Completada / Anulada                     |

---

## ⚙️ Operaciones CRUD

Cada colección incluye las siguientes operaciones:

| Operación          | Método MongoDB         |
|--------------------|------------------------|
| Insertar un dato   | `insertOne()`          |
| Insertar varios    | `insertMany()`         |
| Actualizar         | `updateOne()`          |
| Eliminar           | `deleteOne()` / `deleteMany()` |

---

## 🔍 Consultas

| # | Descripción |
|---|-------------|
| 1 | Cantidad total de prendas vendidas agrupadas **por fecha** |
| 2 | Cantidad de prendas vendidas **filtrando por una fecha específica** |
| 3 | Prendas **más vendidas** ordenadas de mayor a menor |
| 4 | Listado de **productos activos** con stock disponible |
| 5 | **Historial de compras** de un cliente específico |
| 6 | **Ingreso total por categoría** de prenda |

---

## 🚀 Cómo ejecutar

1. Asegurarse de tener **MongoDB** instalado y corriendo:
   ```bash
   mongod --dbpath /data/db
   ```

2. Abrir **MongoDB Shell** (`mongosh`) y ejecutar el archivo:
   ```bash
   mongosh tienda_ropa.js
   ```

   O bien cargarlo desde dentro del shell:
   ```js
   load("tienda_ropa.js")
   ```

3. Verificar las colecciones creadas:
   ```js
   use("tienda_ropa")
   show collections
   ```

---

## 🛠️ Tecnologías

- **MongoDB** — Base de datos NoSQL
- **GitHub** — Control de versiones
- **Markdown** — Documentación

---

## 👤 Autor

Proyecto desarrollado por Melany Villarreal.
