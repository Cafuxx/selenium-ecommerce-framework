from datetime import datetime


def get_timestamp():

    return datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )
    
def build_screenshot_name(test_name):

    return f"{test_name}.png"

import random
import string


def generate_random_text(length=8):

    return "".join(
        random.choice(
            string.ascii_letters
        )
        for _ in range(length)
    )