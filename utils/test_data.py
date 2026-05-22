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
    )
]