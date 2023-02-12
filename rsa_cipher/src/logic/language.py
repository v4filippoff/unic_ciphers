import enum
import string

from src.logic.exceptions import NotAllowedCharacterError, EmptyTextError, NotCorrectNumberToCorrect

OFFSET = 10


class Language(enum.Enum):
    RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper() + string.digits + '!?,.' + string.whitespace
    EN = string.ascii_lowercase + string.ascii_uppercase + string.digits + '!?,.' + string.whitespace


def convert_str_to_int(text: str, language: Language) -> int:
    if not text:
        raise EmptyTextError()
    if set(text) - set(language.value):
        raise NotAllowedCharacterError()
    return int(''.join(str(language.value.find(s) + OFFSET) for s in text))


def convert_int_to_str(number_int: int, language: Language) -> str:
    str_number = str(number_int)
    if not number_int or len(str_number) % 2 == 1:
        raise NotCorrectNumberToCorrect()
    try:
        return ''.join(language.value[int(str_number[i:i+2]) - OFFSET] for i in range(0, len(str_number), 2))
    except IndexError:
        raise NotCorrectNumberToCorrect()


if __name__ == '__main__':
    number = convert_str_to_int('dfgfjeidfsdfgdfhsfdggdfgsdfg', Language.EN)
    print(number)
    message = convert_int_to_str(number, Language.EN)
    print(message)
