# model.py

def estimate_price(area_m2: float, rooms: int, neighborhood_quality: float) -> float:
    """
    Calcula un precio estimado de casa.
    Fórmula inventada, pero consistente:
    - área aporta 1200 USD por m2
    - cada cuarto agrega 8000 USD
    - calidad del barrio (1-5) multiplica el total en un pequeño % extra
    """
    base_price = area_m2 * 1200 + rooms * 8000
    quality_factor = 1 + (neighborhood_quality * 0.03)  # +3% por punto de calidad
    return round(base_price * quality_factor, 2)
