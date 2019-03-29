import difflib
from PyQt5.QtWidgets import QStyleFactory

available_styles = QStyleFactory.keys()


def closest_match(string):
    try:
        value = difflib.get_close_matches(string, available_styles, n=1)[0]
    except IndexError:
        return None

    return value
