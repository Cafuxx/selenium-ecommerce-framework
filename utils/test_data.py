VALID_USERS = [
    (
        "standard_user",
        "secret_sauce"
    ),
    (
        "problem_user",
        "secret_sauce"
    ),
    (
        "performance_glitch_user",
        "secret_sauce"
    )
]


INVALID_LOGIN_DATA = [
    (
        "standard_user",
        "wrong_password",
        "Epic sadface: Username and password do not match any user in this service"
    ),
    (
        "",
        "secret_sauce",
        "Epic sadface: Username is required"
    ),
    (
        "standard_user",
        "",
        "Epic sadface: Password is required"
    ),
    (
        "locked_out_user",
        "secret_sauce",
        "Epic sadface: Sorry, this user has been locked out."
    )
]

INVALID_CHECKOUT_DATA = [

    (
        "",
        "Perez",
        "12345",
        "Error: First Name is required"
    ),

    (
        "Juan",
        "",
        "12345",
        "Error: Last Name is required"
    ),

    (
        "Juan",
        "Perez",
        "",
        "Error: Postal Code is required"
    )
]

PRODUCTS = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
]