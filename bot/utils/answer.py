import re


def answer(message: str) -> str | None:
    if message == "сак" or message == "Сак":
        return "Сам сак"
    elif re.fullmatch("•*", message) or re.fullmatch(
        "[М, м][Д, д][Э, э, А, а, Е, е]*", message
    ):
        return message
    return None
