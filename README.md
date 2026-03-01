# ☕ Coffee Shop Stores API

REST API untuk data lokasi outlet Coffee Shop — untuk latihan konsumsi API.

## Endpoints

| Method | Path | Deskripsi |
|--------|------|-----------|
| GET | `/` | Halaman utama, daftar endpoint |
| GET | `/api/stores` | Semua lokasi (filter: `?type=retail&city=Jakarta Selatan&neighborhood=SCBD`) |
| GET | `/api/stores/{id}` | Detail satu lokasi (contoh: `/api/stores/3`, `/api/stores/HQ`) |
| GET | `/api/stores/type/{type}` | Semua lokasi berdasarkan tipe (contoh: `/api/stores/type/retail`) |
| GET | `/api/stores/nearby?lat=-6.22&lng=106.83&radius=3` | Cari lokasi terdekat dalam radius (km) |
| GET | `/docs` | Swagger UI — dokumentasi interaktif |
| GET | `/redoc` | ReDoc — dokumentasi alternatif |

## Deploy ke Vercel

### 1. Install Vercel CLI
```bash
npm install -g vercel
```

### 2. Login
```bash
vercel login
```

### 3. Deploy
```bash
cd stores-api
vercel --prod
```

Selesai! Vercel akan memberikan URL seperti:
```
https://stores-api-xxxxx.vercel.app
```

### Alternatif: Deploy via GitHub
1. Push folder ini ke repository GitHub
2. Buka https://vercel.com → New Project → Import repo
3. Klik Deploy — otomatis jalan

## Contoh Akses dari Peserta

### Python (requests)
```python
import requests

# Semua stores
url = "https://stores-api-xxxxx.vercel.app"
response = requests.get(f"{url}/api/stores")
data = response.json()
print(data)

# Filter retail saja
response = requests.get(f"{url}/api/stores", params={"type": "retail"})
print(response.json())

# Detail satu store
response = requests.get(f"{url}/api/stores/3")
print(response.json())

# Nearby
response = requests.get(f"{url}/api/stores/nearby", params={"lat": -6.22, "lng": 106.83, "radius": 3})
print(response.json())
```

### R (httr2)
```r
library(httr2)
library(jsonlite)

base_url <- "https://stores-api-xxxxx.vercel.app"

# Semua stores
resp <- request(paste0(base_url, "/api/stores")) |> req_perform()
data <- resp |> resp_body_json()
print(data)

# Filter retail
resp <- request(paste0(base_url, "/api/stores")) |>
  req_url_query(type = "retail") |>
  req_perform()
print(resp |> resp_body_json())

# Detail satu store
resp <- request(paste0(base_url, "/api/stores/3")) |> req_perform()
print(resp |> resp_body_json())

# Nearby
resp <- request(paste0(base_url, "/api/stores/nearby")) |>
  req_url_query(lat = -6.22, lng = 106.83, radius = 3) |>
  req_perform()
print(resp |> resp_body_json())
```

### cURL
```bash
# Semua stores
curl https://stores-api-xxxxx.vercel.app/api/stores

# Filter
curl "https://stores-api-xxxxx.vercel.app/api/stores?type=retail&city=Jakarta+Selatan"

# Detail
curl https://stores-api-xxxxx.vercel.app/api/stores/3

# Nearby
curl "https://stores-api-xxxxx.vercel.app/api/stores/nearby?lat=-6.22&lng=106.83&radius=5"
```

## Struktur Project

```
stores-api/
├── api/
│   └── index.py          # FastAPI app (serverless function)
├── requirements.txt      # Dependencies
├── vercel.json          # Routing config
└── README.md
```
