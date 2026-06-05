# Selenium Ecommerce Framework

[![Tests](https://github.com/Cafuxx/selenium-ecommerce-framework/actions/workflows/selenium.yml/badge.svg)](https://github.com/Cafuxx/selenium-ecommerce-framework/actions)

QA automation framework developed with Python, Selenium, and Pytest using SauceDemo as a practice application.

I started this project to learn web test automation from scratch. As I progressed, I gradually incorporated concepts commonly used in real-world projects, such as the Page Object Model, test parameterization, automated reporting, and continuous execution through GitHub Actions.

Application used for testing:

https://www.saucedemo.com/

---

## Technologies Used

* Python
* Selenium WebDriver
* Pytest
* Pytest HTML
* WebDriver Manager
* GitHub Actions

---

## Implemented Features

* Page Object Model (POM) architecture
* Reusable BasePage class
* Test organization by modules
* Pytest parameterization
* Markers (`smoke` and `regression`)
* Positive and negative test cases
* HTML reports
* Automatic screenshots on failures
* Continuous Integration with GitHub Actions
* Headless execution for CI/CD

---

## Project Structure

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

## Automated Test Cases

### Login

* Successful login
* Locked-out user
* Incorrect password
* Empty username
* Empty password

### Cart

* Add product to cart
* Remove product from cart
* Validation of added products
* Add multiple products
* Empty the entire cart

### Checkout

* Successful checkout
* Required field validation
* Error messages for incomplete information

### Inventory

* Sort products by price (low to high)
* Product sorting verification

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Cafuxx/selenium-ecommerce-framework.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Tests

Run the entire test suite:

```bash
pytest -v
```

Run only smoke tests:

```bash
pytest -m smoke
```

Run only regression tests:

```bash
pytest -m regression
```

Run with shortened traceback output:

```bash
pytest -v --tb=short
```

---

## HTML Reports

Generate an HTML report:

```bash
pytest --html=report.html --self-contained-html
```

The report includes:

* Executed tests
* Passed and failed tests
* Execution time
* Error details

---

## Continuous Integration

This project uses GitHub Actions to automatically run the test suite on every push to the main branch.

This helps ensure that new changes do not break existing functionality and maintains consistent execution across both local and CI environments.

---

## Screenshots

### GitHub Actions

### HTML Report

---

## Key Learnings

During the development of this project, I practiced:

* End-to-end (E2E) automation with Selenium
* Page Object design and maintenance
* Using explicit waits
* Test parameterization
* Negative testing
* Automation framework organization
* Continuous Integration with GitHub Actions
* Automated report generation
* Using Git and GitHub for version control

---

## Next Steps

* Expand negative test scenario coverage
* Add more checkout validations
* Implement additional filter and sorting tests
* Improve test data reusability
* Increase functional coverage of the purchasing workflow
