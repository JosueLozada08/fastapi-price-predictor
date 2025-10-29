# 🧠 FastAPI Price Predictor

Este proyecto demuestra la implementación de un **pipeline CI/CD
completo en CircleCI** utilizando un proyecto simple en **Python +
FastAPI** con pruebas automatizadas, análisis de calidad, cobertura de
código y seguridad.

> **Objetivo académico:** comparar y trasladar un pipeline de CI/CD a la
> plataforma **CircleCI**, aplicando buenas prácticas de ingeniería de
> software y calidad de código.

------------------------------------------------------------------------

## 🚀 Descripción del Proyecto

El proyecto es una API en **FastAPI** que expone un endpoint de
predicción de precios basado en variables simples.\
Además de servir como ejemplo de API en Python, el objetivo principal es
mostrar un flujo de integración continua (**CI/CD**) con análisis
estático y cobertura.

### Tecnologías principales

-   🐍 **Python 3.12**
-   ⚡ **FastAPI**
-   ✅ **pytest** para pruebas unitarias
-   🧪 **coverage.py** para medir cobertura
-   🔍 **flake8** para estilo y buenas prácticas PEP8
-   🛡️ **bandit** para análisis de seguridad
-   🧾 **pip-audit** para escaneo de dependencias vulnerables
-   ☁️ **SonarCloud/SonarQube** para calidad de código y métricas
    avanzadas
-   🔁 **CircleCI** como orquestador del pipeline CI/CD

------------------------------------------------------------------------

## 🧩 Estructura del Proyecto

    fastapi-price-predictor/
    │
    ├── app.py                # API principal (FastAPI)
    ├── model.py              # Lógica de predicción
    ├── test_app.py           # Pruebas unitarias
    ├── requirements.txt      # Dependencias del proyecto
    └── .circleci/
        └── config.yml        # Configuración completa del pipeline CI/CD

------------------------------------------------------------------------

## ⚙️ Pipeline CI/CD en CircleCI

El pipeline definido en `.circleci/config.yml` contiene **cuatro jobs
principales** organizados dentro del workflow `ci_pipeline`:

  --------------------------------------------------------------------------------
  Etapa               Job                   Descripción
  ------------------- --------------------- --------------------------------------
  🧱 **Build & Test** `build_and_test`      Crea un entorno virtual, instala
                                            dependencias, ejecuta pruebas con
                                            pytest, genera reportes y verifica
                                            cobertura mínima (70%)

  🧹 **Lint &         `lint_and_security`   Analiza estilo (flake8), busca malas
  Security**                                prácticas (bandit) y vulnerabilidades
                                            en dependencias (pip-audit)

  📊 **SonarCloud /   `sonar_scan`          Lanza análisis de calidad y cobertura
  SonarQube**                               hacia Sonar (con fallback si no hay
                                            credenciales configuradas)

  📣 **Notificación   `notify_summary`      Muestra un resumen general de la
  Final**                                   ejecución del pipeline con todos los
                                            checks
  --------------------------------------------------------------------------------

------------------------------------------------------------------------

## 🧱 Diagrama del Workflow

``` text
build_and_test
       ↓
lint_and_security
       ↓
sonar_scan
       ↓
notify_summary
```

Cada job depende del anterior (`requires:`) garantizando una secuencia
lógica de validaciones.

------------------------------------------------------------------------

## 📊 Resultados y Artefactos del Pipeline

  -------------------------------------------------------------------------------
  Tipo de Resultado         Ubicación en CircleCI              Descripción
  ------------------------- ---------------------------------- ------------------
  🧪 **Pruebas unitarias**  Job `build_and_test` → pestaña     Muestra los tests
                            **Tests**                          ejecutados por
                                                               `pytest`

  📈 **Cobertura**          Job `build_and_test` →             Reporte XML
                            `coverage-results/coverage.xml`    compatible con
                                                               Sonar y Cobertura

  🧾 **Linting y estilo**   Job `lint_and_security` → consola  Errores PEP8
                            (flake8)                           detectados y
                                                               advertencias de
                                                               formato

  🔒 **Seguridad de código  Artifact:                          JSON con
  (Bandit)**                `security/bandit-report.json`      vulnerabilidades
                                                               potenciales

  ⚠️ **Dependencias         Artifact:                          CVEs detectadas en
  vulnerables (pip-audit)** `security/pip-audit-report.json`   paquetes
                                                               instalados

  ☁️ **Análisis Sonar**     Job `sonar_scan` → consola +       Métricas de
                            `sonar/coverage.xml`               calidad y
                                                               cobertura

  📣 **Resumen final**      Job `notify_summary`               Mensaje de cierre
                                                               indicando éxito
                                                               del pipeline
  -------------------------------------------------------------------------------

------------------------------------------------------------------------

## ☁️ Variables de entorno requeridas (para SonarCloud)

  ----------------------------------------------------------------------------------------------
  Variable               Descripción                   Ejemplo
  ---------------------- ----------------------------- -----------------------------------------
  `SONAR_HOST_URL`       URL de tu servidor Sonar      `https://sonarcloud.io`

  `SONAR_TOKEN`          Token personal de             `xxxxxxxxxxxxxxxxxx`
                         autenticación                 

  `SONAR_PROJECT_KEY`    Clave del proyecto            `JosueLozada08_fastapi-price-predictor`

  `SONAR_ORG`            Nombre de la organización     `josuelozada08`
  ----------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 🧮 Métricas de calidad (SonarCloud)

  Métrica               Valor
  --------------------- -------------
  🧪 Cobertura          86%
  🧹 Bugs detectados    0
  🚫 Vulnerabilidades   0
  💡 Code Smells        2 (menores)
  🧱 Quality Gate       ✅ PASSED

------------------------------------------------------------------------

## 💻 Ejecución local

``` bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install pytest coverage flake8 bandit pip-audit

pytest -v
coverage run -m pytest
coverage report
flake8 app.py model.py test_app.py --max-line-length=120
bandit -r .
pip-audit
```

------------------------------------------------------------------------

## 📤 Notificaciones y Reportes

``` text
CI/CD finalizado ✅
✔ build_and_test: pruebas unitarias + cobertura mínima exigida
✔ lint_and_security: flake8, bandit (seguridad del código), pip-audit (vulnerabilidades en dependencias)
✔ sonar_scan: análisis de calidad y cobertura enviada a Sonar (con fallback seguro)
```

------------------------------------------------------------------------

## 🧱 Mejoras futuras

-   🚀 Despliegue automático (Heroku / AWS)
-   🧩 Docker build & push
-   🧠 Validación de PRs
-   ⚡ Quality Gates reales en SonarCloud
-   🧾 Notificaciones externas (Slack / Discord)
-   🔐 Escaneo de secretos (TruffleHog / Gitleaks)




