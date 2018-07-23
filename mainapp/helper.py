import re


def check_password_strength(password):
    pattern = r"(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$"
    match = re.match(pattern, password)
    return match