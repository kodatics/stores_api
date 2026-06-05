from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import HTMLResponse
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
  {
    "sales_outlet_id": 1,
    "sales_outlet_type": "headquarters",
    "store_address": "Jl. Gatot Subroto Kav. 99",
    "store_city": "Jakarta Selatan",
    "store_state_province": "DKI Jakarta",
    "store_telephone": "021-5298000",
    "store_postal_code": 12930,
    "store_longitude": 106.8156,
    "store_latitude": -6.2357,
    "manager": 0,
    "neighborhood": "Kuningan"
  },
  {
    "sales_outlet_id": 2,
    "sales_outlet_type": "warehouse",
    "store_address": "Kawasan Industri Pulo Gadung Blok C No.12",
    "store_city": "Jakarta Timur",
    "store_state_province": "DKI Jakarta",
    "store_telephone": "021-4616100",
    "store_postal_code": 13930,
    "store_longitude": 106.9112,
    "store_latitude": -6.1875,
    "manager": 0,
    "neighborhood": "Cakung"
  },
  {
    "sales_outlet_id": 3,
    "sales_outlet_type": "retail",
    "store_address": "Jl. Sudirman No. 21 SCBD",
    "store_city": "Jakarta Selatan",
    "store_state_province": "DKI Jakarta",
    "store_telephone": "021-5201234",
    "store_postal_code": 12190,
    "store_longitude": 106.8073,
    "store_latitude": -6.2241,
    "manager": 1,
    "neighborhood": "SCBD"
  },
  {
    "sales_outlet_id": 4,
    "sales_outlet_type": "retail",
    "store_address": "Jl. Senopati No. 10",
    "store_city": "Jakarta Selatan",
    "store_state_province": "DKI Jakarta",
    "store_telephone": "021-5201890",
    "store_postal_code": 12110,
    "store_longitude": 106.8011,
    "store_latitude": -6.2365,
    "manager": 0,
    "neighborhood": "Senopati"
  },
  {
    "sales_outlet_id": 5,
    "sales_outlet_type": "retail",
    "store_address": "Jl. Thamrin No. 5 Grand Indonesia Lt.2",
    "store_city": "Jakarta Pusat",
    "store_state_province": "DKI Jakarta",
    "store_telephone": "021-3901567",
    "store_postal_code": 10310,
    "store_longitude": 106.8219,
    "store_latitude": -6.1944,
    "manager": 15,
    "neighborhood": "Thamrin"
  },
  {
    "sales_outlet_id": 6,
    "sales_outlet_type": "retail",
    "store_address": "Jl. Melawai No. 26",
    "store_city": "Jakarta Selatan",
    "store_state_province": "DKI Jakarta",
    "store_telephone": "021-7269123",
    "store_postal_code": 12160,
    "store_longitude": 106.7993,
    "store_latitude": -6.2444,
    "manager": 0,
    "neighborhood": "Melawai"
  },
  {
    "sales_outlet_id": 7,
    "sales_outlet_type": "retail",
    "store_address": "Jl. Tebet Barat Dalam No. 5",
    "store_city": "Jakarta Selatan",
    "store_state_province": "DKI Jakarta",
    "store_telephone": "021-8291234",
    "store_postal_code": 12810,
    "store_longitude": 106.8445,
    "store_latitude": -6.241,
    "manager": 0,
    "neighborhood": "Tebet"
  },
  {
    "sales_outlet_id": 8,
    "sales_outlet_type": "retail",
    "store_address": "Jl. Kemang Raya No. 58",
    "store_city": "Jakarta Selatan",
    "store_state_province": "DKI Jakarta",
    "store_telephone": "021-7198234",
    "store_postal_code": 12730,
    "store_longitude": 106.8127,
    "store_latitude": -6.2648,
    "manager": 28,
    "neighborhood": "Kemang"
  },
  {
    "sales_outlet_id": 9,
    "sales_outlet_type": "retail",
    "store_address": "Jl. Cikajang No. 17 Kebayoran Baru",
    "store_city": "Jakarta Selatan",
    "store_state_province": "DKI Jakarta",
    "store_telephone": "021-7241567",
    "store_postal_code": 12170,
    "store_longitude": 106.7966,
    "store_latitude": -6.2386,
    "manager": 0,
    "neighborhood": "Kebayoran Baru"
  },
  {
    "sales_outlet_id": 10,
    "sales_outlet_type": "retail",
    "store_address": "Jl. Ciracas Raya No. 34",
    "store_city": "Jakarta Timur",
    "store_state_province": "DKI Jakarta",
    "store_telephone": "021-8709876",
    "store_postal_code": 13740,
    "store_longitude": 106.8945,
    "store_latitude": -6.3112,
    "manager": 0,
    "neighborhood": "Ciracas"
  },
  {
    "sales_outlet_id": 11,
    "sales_outlet_type": "retail",
    "store_address": "Jl. RE Martadinata No. 6 Ancol",
    "store_city": "Jakarta Utara",
    "store_state_province": "DKI Jakarta",
    "store_telephone": "021-6471234",
    "store_postal_code": 14430,
    "store_longitude": 106.8392,
    "store_latitude": -6.1237,
    "manager": 0,
    "neighborhood": "Ancol"
  },
  {
    "sales_outlet_id": 99,
    "sales_outlet_type": "fulfillment",
    "store_address": "Jl. Rawa Belong No. 11",
    "store_city": "Jakarta Barat",
    "store_state_province": "DKI Jakarta",
    "store_telephone": "021-5348700",
    "store_postal_code": 11540,
    "store_longitude": 106.7701,
    "store_latitude": -6.1987,
    "manager": 0,
    "neighborhood": "Rawa Belong"
  }
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

# Data endpoint Anda
api_info = {
    "message": "☕ Coffee Shop Stores API",
    "version": "1.0.0",
    "endpoints": [
        {"method": "GET", "path": "/api/stores", "description": "Semua lokasi (filter: ?type=retail&city=Jakarta Selatan&neighborhood=SCBD)"},
        {"method": "GET", "path": "/api/stores/{id}", "description": "Detail satu lokasi berdasarkan ID"},
        {"method": "GET", "path": "/api/stores/type/retail", "description": "Shortcut: semua outlet retail"},
        {"method": "GET", "path": "/api/stores/nearby?lat=-6.22&lng=106.83&radius=3", "description": "Cari lokasi terdekat dalam radius (km)"},
        {"method": "GET", "path": "/docs", "description": "Swagger UI — dokumentasi interaktif"}
    ]
}

# ============================================================
# ENDPOINTS
# ============================================================

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # Membuat baris tabel secara dinamis dari api_info
    rows = ""
    for ep in api_info["endpoints"]:
        rows += f"""
        <tr class="border-b border-slate-700 hover:bg-slate-700/30 transition">
            <td class="py-4 px-4"><span class="bg-green-500/20 text-green-400 text-xs font-bold px-2 py-1 rounded">{ep['method']}</span></td>
            <td class="py-4 px-4 font-mono text-indigo-300 text-sm">{ep['path']}</td>
            <td class="py-4 px-4 text-slate-400 text-sm">{ep['description']}</td>
        </tr>
        """

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Coffee Shop API</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-slate-900 text-slate-200 min-h-screen flex items-center justify-center p-6">
        <div class="max-w-4xl w-full bg-slate-800 rounded-2xl shadow-2xl border border-slate-700 overflow-hidden">
            <div class="p-8 border-b border-slate-700 bg-gradient-to-r from-slate-800 to-slate-700">
                <div class="flex justify-between items-center">
                    <div>
                        <h1 class="text-3xl font-bold text-white mb-2">{api_info['message']}</h1>
                        <p class="text-slate-400 italic font-medium">Empowering data-driven decision for your caffeine needs.</p>
                    </div>
                    <span class="bg-indigo-600 text-white text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider">v{api_info['version']}</span>
                </div>
            </div>
            
            <div class="p-8">
                <h2 class="text-xl font-semibold text-indigo-400 mb-4">Available Endpoints</h2>
                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse">
                        <thead>
                            <tr class="text-slate-500 uppercase text-xs tracking-widest border-b border-slate-700">
                                <th class="pb-3 px-4">Method</th>
                                <th class="pb-3 px-4">Endpoint</th>
                                <th class="pb-3 px-4">Description</th>
                            </tr>
                        </thead>
                        <tbody>
                            {rows}
                        </tbody>
                    </table>
                </div>
                
                <div class="mt-8 flex gap-4">
                    <a href="/docs" class="bg-indigo-600 hover:bg-indigo-500 text-white px-6 py-2 rounded-lg font-semibold transition shadow-lg shadow-indigo-500/20">
                        🚀 Open Swagger UI to Try
                    </a>
                </div>
            </div>
            
            <div class="bg-slate-900/50 p-4 text-center text-xs text-slate-500 border-t border-slate-700">
                &copy; 2026 Kodatics Analytics • Powered by FastAPI & Vercel
            </div>
        </div>
    </body>
    </html>
    """


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
