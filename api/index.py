from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import math

# ============================================================
# APP
# ============================================================
app = FastAPI(
    title="Coffee Shop Stores API",
    description="REST API untuk data lokasi outlet Coffee Shop — untuk latihan konsumsi API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# DATA
# ============================================================
STORES = [
    {"sales_outlet_id": "0", "sales_outlet_type": "none", "store_address": "-", "store_city": "-", "store_state_province": "-", "store_telephone": "-", "store_postal_code": "-", "store_longitude": None, "store_latitude": None, "manager": None, "neighborhood": "-"},
    {"sales_outlet_id": "3", "sales_outlet_type": "retail", "store_address": "Jl. Sudirman No. 45", "store_city": "Jakarta Selatan", "store_state_province": "DKI Jakarta", "store_telephone": "021-5551234", "store_postal_code": "12190", "store_longitude": 106.823, "store_latitude": -6.2088, "manager": 8, "neighborhood": "SCBD"},
    {"sales_outlet_id": "4", "sales_outlet_type": "retail", "store_address": "Jl. Thamrin No. 28", "store_city": "Jakarta Pusat", "store_state_province": "DKI Jakarta", "store_telephone": "021-5552345", "store_postal_code": "10350", "store_longitude": 106.8228, "store_latitude": -6.1944, "manager": 28, "neighborhood": "Thamrin"},
    {"sales_outlet_id": "5", "sales_outlet_type": "retail", "store_address": "Jl. Gatot Subroto Kav. 12", "store_city": "Jakarta Selatan", "store_state_province": "DKI Jakarta", "store_telephone": "021-5559876", "store_postal_code": "12930", "store_longitude": 106.8296, "store_latitude": -6.2349, "manager": 15, "neighborhood": "Kuningan"},
    {"sales_outlet_id": "6", "sales_outlet_type": "retail", "store_address": "Jl. Senopati No. 72", "store_city": "Jakarta Selatan", "store_state_province": "DKI Jakarta", "store_telephone": "021-5553456", "store_postal_code": "12110", "store_longitude": 106.8095, "store_latitude": -6.2273, "manager": 33, "neighborhood": "Senopati"},
    {"sales_outlet_id": "7", "sales_outlet_type": "retail", "store_address": "Jl. Panglima Polim No. 15", "store_city": "Jakarta Selatan", "store_state_province": "DKI Jakarta", "store_telephone": "021-5554567", "store_postal_code": "12160", "store_longitude": 106.7985, "store_latitude": -6.2442, "manager": 38, "neighborhood": "Melawai"},
    {"sales_outlet_id": "8", "sales_outlet_type": "retail", "store_address": "Jl. Kemang Raya No. 18", "store_city": "Jakarta Selatan", "store_state_province": "DKI Jakarta", "store_telephone": "021-5555678", "store_postal_code": "12730", "store_longitude": 106.8137, "store_latitude": -6.2615, "manager": 22, "neighborhood": "Kemang"},
    {"sales_outlet_id": "9", "sales_outlet_type": "retail", "store_address": "Jl. Casablanca Raya No. 88", "store_city": "Jakarta Selatan", "store_state_province": "DKI Jakarta", "store_telephone": "021-5556789", "store_postal_code": "12870", "store_longitude": 106.8413, "store_latitude": -6.2297, "manager": 43, "neighborhood": "Tebet"},
    {"sales_outlet_id": "10", "sales_outlet_type": "retail", "store_address": "Jl. Wolter Monginsidi No. 33", "store_city": "Jakarta Selatan", "store_state_province": "DKI Jakarta", "store_telephone": "021-5557890", "store_postal_code": "12170", "store_longitude": 106.8022, "store_latitude": -6.2365, "manager": 48, "neighborhood": "Kebayoran Baru"},
    {"sales_outlet_id": "HQ", "sales_outlet_type": "headquarters", "store_address": "Jl. HR Rasuna Said Kav. C-5", "store_city": "Jakarta Selatan", "store_state_province": "DKI Jakarta", "store_telephone": "021-5550001", "store_postal_code": "12940", "store_longitude": 106.834, "store_latitude": -6.2255, "manager": 2, "neighborhood": "Kuningan"},
    {"sales_outlet_id": "WH", "sales_outlet_type": "warehouse", "store_address": "Jl. Raya Cakung Cilincing No. 10", "store_city": "Jakarta Utara", "store_state_province": "DKI Jakarta", "store_telephone": "021-5550002", "store_postal_code": "14130", "store_longitude": 106.9345, "store_latitude": -6.158, "manager": 3, "neighborhood": "Cakung"},
    {"sales_outlet_id": "FL", "sales_outlet_type": "fulfillment", "store_address": "Jl. Raya Bogor KM 26", "store_city": "Jakarta Timur", "store_state_province": "DKI Jakarta", "store_telephone": "021-5550003", "store_postal_code": "13710", "store_longitude": 106.8756, "store_latitude": -6.332, "manager": 53, "neighborhood": "Ciracas"},
]

# ============================================================
# HELPER
# ============================================================
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    return R * 2 * math.asin(math.sqrt(a))

# ============================================================
# ENDPOINTS
# ============================================================

@app.get("/")
def root():
    """Halaman utama — daftar endpoint yang tersedia."""
    return {
        "message": "☕ Coffee Shop Stores API",
        "version": "1.0.0",
        "endpoints": [
            {"method": "GET", "path": "/api/stores",            "description": "Semua lokasi (filter: ?type=retail&city=Jakarta Selatan&neighborhood=SCBD)"},
            {"method": "GET", "path": "/api/stores/{id}",       "description": "Detail satu lokasi berdasarkan ID (contoh: /api/stores/3)"},
            {"method": "GET", "path": "/api/stores/type/retail", "description": "Shortcut: semua outlet retail"},
            {"method": "GET", "path": "/api/stores/nearby?lat=-6.22&lng=106.83&radius=3", "description": "Cari lokasi terdekat dalam radius (km)"},
            {"method": "GET", "path": "/docs",                  "description": "Swagger UI — dokumentasi interaktif"},
        ]
    }


@app.get("/api/stores")
def get_stores(
    type: Optional[str] = Query(None, description="Filter by type: retail, headquarters, warehouse, fulfillment (comma-separated)"),
    city: Optional[str] = Query(None, description="Filter by city, e.g. 'Jakarta Selatan'"),
    neighborhood: Optional[str] = Query(None, description="Filter by neighborhood, e.g. 'SCBD'"),
):
    """
    Ambil daftar semua lokasi.

    Bisa difilter menggunakan query parameters:
    - **type**: retail, headquarters, warehouse, fulfillment (bisa comma-separated)
    - **city**: nama kota (partial match)
    - **neighborhood**: nama kawasan (partial match)
    """
    result = [s for s in STORES if s["sales_outlet_type"] != "none"]

    if type:
        types = [t.strip().lower() for t in type.split(",")]
        result = [s for s in result if s["sales_outlet_type"] in types]

    if city:
        result = [s for s in result if city.lower() in s["store_city"].lower()]

    if neighborhood:
        result = [s for s in result if neighborhood.lower() in s["neighborhood"].lower()]

    return {"status": "success", "count": len(result), "data": result}


@app.get("/api/stores/type/{store_type}")
def get_stores_by_type(store_type: str):
    """
    Shortcut: ambil semua lokasi berdasarkan tipe.

    Contoh: /api/stores/type/retail
    """
    result = [s for s in STORES if s["sales_outlet_type"] == store_type.lower()]
    if not result:
        raise HTTPException(status_code=404, detail=f"No stores found with type '{store_type}'")
    return {"status": "success", "count": len(result), "data": result}


@app.get("/api/stores/nearby")
def get_nearby_stores(
    lat: float = Query(..., description="Latitude, contoh: -6.22"),
    lng: float = Query(..., description="Longitude, contoh: 106.83"),
    radius: float = Query(5.0, description="Radius pencarian dalam km (default: 5)"),
):
    """
    Cari lokasi dalam radius tertentu dari koordinat.

    Mengembalikan daftar lokasi yang diurutkan dari yang terdekat,
    lengkap dengan jarak (distance_km).
    """
    result = []
    for s in STORES:
        if s["store_latitude"] is None:
            continue
        dist = haversine(lat, lng, s["store_latitude"], s["store_longitude"])
        if dist <= radius:
            result.append({**s, "distance_km": round(dist, 2)})

    result.sort(key=lambda x: x["distance_km"])
    return {"status": "success", "count": len(result), "data": result}


@app.get("/api/stores/{store_id}")
def get_store_by_id(store_id: str):
    """
    Ambil detail satu lokasi berdasarkan ID.

    Contoh: /api/stores/3, /api/stores/HQ
    """
    store = next((s for s in STORES if s["sales_outlet_id"] == store_id), None)
    if not store:
        raise HTTPException(status_code=404, detail=f"Store with ID '{store_id}' not found")
    return {"status": "success", "data": store}
