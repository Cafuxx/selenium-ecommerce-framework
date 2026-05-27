# Selenium Ecommerce Framework

![Tests](https://github.com/Cafuxx/https://github.com/Cafuxx/selenium-ecommerce-framework.git/actions/workflows/selenium.yml/badge.svg)

Proyecto personal de automatización QA usando Selenium, Pytest y Python.  
El objetivo principal de este framework fue practicar automatización E2E aplicando buenas prácticas reales de testing y estructura de proyectos.

La aplicación utilizada para las pruebas es:

https://www.saucedemo.com/

---

## Stack utilizado

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Allure Reports
- WebDriver Manager
- GitHub Actions

---

## Qué incluye el proyecto

- Arquitectura Page Object Model (POM)
- BasePage reutilizable
- Tests organizados por módulos
- Parametrización con Pytest
- Markers (`smoke` y `regression`)
- Negative testing
- Reportes HTML
- Allure Reports
- Screenshots automáticos en fallos
- CI/CD con GitHub Actions

---

## Estructura del proyecto

```plaintext
selenium-ecommerce-framework/
│
├── pages/
├── tests/
│   ├── login/
│   ├── cart/
│   ├── checkout/
│   └── inventory/
│
├── utils/
├── screenshots/
├── .github/workflows/
├── conftest.py
├── pytest.ini
└── requirements.txt
```

---

## Casos de prueba implementados

### Login
- Login válido
- Password incorrecta
- Usuario vacío
- Password vacía
- Usuario bloqueado

### Cart
- Agregar producto al carrito
- Eliminar producto
- Validación del carrito
- Agregar múltiples productos
- Eliminar todos los productos

### Checkout
- Checkout exitoso
- Validaciones de campos obligatorios
- Mensajes de error

### Inventory
- Ordenar productos por precio
- Ordenar productos alfabéticamente

---

## Instalación

Clonar repositorio:

```bash
git clone https://github.com/TU_USER/TU_REPO.git
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecutar tests

Ejecutar toda la suite:

```bash
pytest -v
```

Ejecutar smoke tests:

```bash
pytest -m smoke
```

Ejecutar regression tests:

```bash
pytest -m regression
```

---

## Reportes HTML

Generar reporte HTML:

```bash
pytest --html=report.html --self-contained-html
```

---

## Allure Reports

Generar resultados:

```bash
pytest --alluredir=allure-results
```

Abrir reporte:

```bash
allure serve allure-results
```

---

## CI/CD

El proyecto utiliza GitHub Actions para ejecutar automáticamente la suite de tests en cada push y pull request.

---

## Algunas cosas que practiqué con este proyecto

- Automatización E2E
- Selenium WebDriver
- Diseño Page Object Model
- Explicit waits
- Data-driven testing
- Negative testing
- Organización de frameworks QA
- Reportes automáticos
- Integración continua con GitHub Actions
- Uso de Git y GitHub en proyectos reales

---

## Screenshots

### GitHub Actions

_Agregar screenshot acá_

### HTML Report

_Agregar screenshot acá_

### Allure Report

_Agregar screenshot acá_