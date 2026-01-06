from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import claims, documents

app = FastAPI(title="FNOL Claims System")

# ✅ CORS MUST be added BEFORE routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for development
    allow_credentials=True,
    allow_methods=["*"],   # THIS enables OPTIONS
    allow_headers=["*"],
)

# ✅ Now include routes
app.include_router(claims.router)
app.include_router(documents.router)

@app.get("/")
def home():
    return {"message": "FNOL system is running"}
