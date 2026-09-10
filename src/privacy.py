import re

def has_email(text):
    return bool(re.search(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{{2,}}", text))
