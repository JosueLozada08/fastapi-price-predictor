# fastapi-price-predictor

## 1. Descripción del proyecto
Este proyecto es una API en Python construida con FastAPI. Expone un modelo sencillo para estimar el precio de una vivienda en función de:
- Metros cuadrados del inmueble
- Número de habitaciones
- Calidad del barrio (escala 1 a 5)

Endpoints principales:
- `GET /health` → Verifica que el servicio está vivo.
- `POST /predict` → Recibe las características de la casa y devuelve un precio estimado.

El modelo de negocio está en `model.py`.  
La API está en `app.py`.  
Las pruebas unitarias están en `test_app.py`.

## 2. Objetivo académico
Este repositorio se usa para demostrar un flujo CI/CD real usando CircleCI:

- Construcción y pruebas automatizadas
- Análisis de calidad de código
- Análisis de seguridad
- Notificación/resumen al final del pipeline

Esto cumple con:
1. "Configura un proyecto en CircleCI con múltiples jobs y workflows"
2. "Traslada tu pipeline de la tarea anterior a Circle CI"
3. "Configurar el envío de notificaciones"

## 3. Pipeline CI/CD (CircleCI)
El pipeline está definido en `.circleci/config.yml`.

### 3.1 Workflow
El workflow se llama `ci_pipeline` y orquesta los jobs en el siguiente orden:

1. `build_and_test`
2. `lint_and_security` (requiere que `build_and_test` haya pasado)
3. `notify_summary` (requiere que `lint_and_security` haya pasado)

Esto asegura que:
- No se hace análisis de calidad si el código ni siquiera compila o pasa tests.
- No se "notifica" éxito si antes hubo fallos.

### 3.2 Jobs

#### a) `build_and_test`
Este job hace lo siguiente:
1. Crea un entorno virtual de Python (`python -m venv venv`).
2. Instala dependencias del proyecto desde `requirements.txt` (FastAPI, Pytest, etc.).
3. Ejecuta las pruebas unitarias con `pytest`.
4. Publica los resultados de las pruebas como `test-results/junit.xml` en CircleCI (test reporting).
5. Sube los resultados como artifacts.

Comando principal:
```bash
pytest --junitxml=test-results/junit.xml
