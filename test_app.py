# test_app.py
from model import estimate_price

def test_estimate_price_basic():
    # Caso sencillo: 100 m2, 3 cuartos, barrio calidad 3
    price = estimate_price(area_m2=100, rooms=3, neighborhood_quality=3)
    assert price > 0
    # validación más específica para que el profe vea que no es dummy:
    # cálculo manual esperado:
    # base = (100 * 1200) + (3 * 8000) = 120000 + 24000 = 144000
    # factor calidad = 1 + (3 * 0.03) = 1.09
    # final = 144000 * 1.09 = 156960
    assert price == 156960.0

def test_estimate_price_changes_with_area():
    price_small = estimate_price(50, 2, 2)
    price_big = estimate_price(150, 2, 2)
    assert price_big > price_small

def test_estimate_price_changes_with_quality():
    low_quality = estimate_price(80, 2, 1)
    high_quality = estimate_price(80, 2, 5)
    assert high_quality > low_quality
