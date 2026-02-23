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
