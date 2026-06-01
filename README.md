# Selenium Ecommerce Framework

[![Tests](https://github.com/Cafuxx/selenium-ecommerce-framework/actions/workflows/selenium.yml/badge.svg)](https://github.com/Cafuxx/selenium-ecommerce-framework/actions)

Framework de automatización QA desarrollado con Python, Selenium y Pytest utilizando SauceDemo como aplicación de práctica.

Comencé este proyecto para aprender automatización de pruebas web desde cero y, a medida que avanzaba, fui incorporando conceptos utilizados en proyectos reales como Page Object Model, parametrización de pruebas, reportes automáticos y ejecución continua mediante GitHub Actions.

Aplicación utilizada para las pruebas:

https://www.saucedemo.com/

---

## Tecnologías utilizadas

* Python
* Selenium WebDriver
* Pytest
* Pytest HTML
* WebDriver Manager
* GitHub Actions

---

## Funcionalidades implementadas

* Arquitectura Page Object Model (POM)
* Clase BasePage reutilizable
* Organización de tests por módulos
* Parametrización con Pytest
* Markers (`smoke` y `regression`)
* Casos positivos y negativos
* Reportes HTML
* Screenshots automáticos en fallos
* Integración continua con GitHub Actions
* Ejecución headless para CI/CD

---

## Estructura del proyecto

```plaintext
selenium-ecommerce-framework/
│
├── .github/
│   └── workflows/
│       └── selenium.yml
│
├── assets/
│   ├── github-actions.png
│   └── report.html
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── reports/
│
├── tests/
│   ├── login/
│   ├── cart/
│   ├── checkout/
│   └── inventory/
│
├── utils/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Casos de prueba automatizados

### Login

* Login exitoso
* Usuario bloqueado
* Contraseña incorrecta
* Usuario vacío
* Contraseña vacía

### Cart

* Agregar producto al carrito
* Eliminar producto del carrito
* Validación de productos agregados
* Agregar múltiples productos
* Vaciar carrito completo

### Checkout

* Checkout exitoso
* Validación de campos obligatorios
* Mensajes de error para datos incompletos

### Inventory

* Ordenar productos por precio (menor a mayor)
* Verificación de ordenamiento de productos

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/Cafuxx/selenium-ecommerce-framework.git
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución de pruebas

Ejecutar toda la suite:

```bash
pytest -v
```

Ejecutar únicamente smoke tests:

```bash
pytest -m smoke
```

Ejecutar únicamente regression tests:

```bash
pytest -m regression
```

Ejecutar con salida resumida:

```bash
pytest -v --tb=short
```

---

## Reportes HTML

Generar reporte HTML:

```bash
pytest --html=report.html --self-contained-html
```

El reporte incluye:

* Tests ejecutados
* Tests aprobados y fallidos
* Tiempo de ejecución
* Detalle de errores

---

## Integración continua

El proyecto utiliza GitHub Actions para ejecutar automáticamente la suite de pruebas en cada push realizado a la rama principal.

Esto permite validar que los cambios no rompan funcionalidades existentes y mantener una ejecución consistente tanto en entorno local como en CI.

---

## Capturas

### GitHub Actions



### Reporte HTML



---

## Aprendizajes obtenidos

Durante el desarrollo de este proyecto practiqué:

* Automatización E2E con Selenium
* Diseño y mantenimiento de Page Objects
* Uso de explicit waits
* Parametrización de pruebas
* Negative testing
* Organización de frameworks de automatización
* Integración continua con GitHub Actions
* Generación de reportes automáticos
* Uso de Git y GitHub para control de versiones

---

## Próximos pasos

* Ampliar cobertura de escenarios negativos
* Incorporar más validaciones de checkout
* Agregar pruebas de filtros y ordenamientos adicionales
* Mejorar la reutilización de datos de prueba
* Incrementar la cobertura funcional del flujo de compra
