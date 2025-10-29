# app.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
from model import estimate_price

app = FastAPI(title="House Price Predictor API",
              version="1.0.0",
              description="API simple para estimar el precio de una casa")

class HouseFeatures(BaseModel):
    area_m2: float = Field(..., gt=0, description="Área construida en m2")
    rooms: int = Field(..., gt=0, description="Número de dormitorios")
    neighborhood_quality: float = Field(..., ge=1, le=5, description="Calidad del barrio de 1 a 5")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict_price(features: HouseFeatures):
    price = estimate_price(
        area_m2=features.area_m2,
        rooms=features.rooms,
        neighborhood_quality=features.neighborhood_quality
    )
    return {
        "estimated_price_usd": price,
        "currency": "USD"
    }
