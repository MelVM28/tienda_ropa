// Crear y usar la base de datos
use tiendaRopaDB

// ============================
// COLECCIÓN: USUARIOS
// ============================

// Insertar un usuario
db.usuarios.insertOne({
    nombre: "Gael Montiel",
    email: "gael.montiel@gmail.com",
    telefono: "8745-2190",
    direccion: "Cartago",
    fechaRegistro: new Date()
})

// Insertar varios usuarios
db.usuarios.insertMany([
    {
        nombre: "Samira Valverde",
        email: "samira.v@gmail.com",
        telefono: "8891-3344",
        direccion: "Puntarenas",
        fechaRegistro: new Date()
    },
    {
        nombre: "Thiago Echeverria",
        email: "thiago.e@gmail.com",
        telefono: "8622-7788",
        direccion: "Guanacaste",
        fechaRegistro: new Date()
    }
])

// Actualizar un usuario
db.usuarios.updateOne(
    { nombre: "Gael Montiel" },
    { $set: { telefono: "8999-0000" } }
)

// Eliminar un usuario
db.usuarios.deleteOne({ nombre: "Thiago Echeverria" })

// ============================
// COLECCIÓN: PRENDAS
// ============================

// Insertar una prenda
db.prendas.insertOne({
    nombre: "Blazer Oversize Lino",
    marca: "Aurelia Studio",
    talla: "M",
    precio: 42000,
    stock: 12
})

// Insertar varias prendas
db.prendas.insertMany([
    {
        nombre: "Cargo Relaxed Fit",
        marca: "Nokari Wear",
        talla: "L",
        precio: 28500,
        stock: 20
    },
    {
        nombre: "Vestido Midi Asimetrico",
        marca: "Aurelia Studio",
        talla: "S",
        precio: 36000,
        stock: 8
    }
])

// Actualizar una prenda
db.prendas.updateOne(
    { nombre: "Cargo Relaxed Fit" },
    { $set: { stock: 18 } }
)

// Eliminar una prenda
db.prendas.deleteOne({ nombre: "Vestido Midi Asimetrico" })

// ============================
// CONSULTAS
// ============================

// Mostrar todas las ventas registradas
// Esta consulta obtiene todos los documentos de la colección ventas
db.ventas.find()

// Obtener ventas realizadas en una fecha específica
// Esta consulta filtra las ventas del 21 de febrero de 2025
db.ventas.find({
    fecha: new Date("2025-02-21")
})

// Obtener la cantidad total de prendas vendidas en una fecha específica
// Esta consulta suma la cantidad de prendas vendidas el 21 de febrero de 2025
db.ventas.aggregate([
    {
        $match: {
            fecha: new Date("2025-02-21")
        }
    },
    {
        $unwind: "$prendas"
    },
    {
        $group: {
            _id: "$fecha",
            totalPrendasVendidas: { $sum: "$prendas.cantidad" }
        }
    }
])

