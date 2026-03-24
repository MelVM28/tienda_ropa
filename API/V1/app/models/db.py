from pymongo import MongoClient

# ── Cambia este string por tu cadena de conexión de Atlas ──────────────────────
MONGO_URI = "mongodb+srv://mel_db:Mel2805db@cluster0.ux5x4h0.mongodb.net/?retryWrites=true&w=majority"
# ──────────────────────────────────────────────────────────────────────────────

client = MongoClient(MONGO_URI)
db     = client["tienda_ropa"]

