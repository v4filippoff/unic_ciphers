import enum
import string

MOST_COMMON_EN = 'e'
MOST_COMMON_RU = 'о'


class LanguageCharacters(enum.Enum):
    EN = 'abcdefghijklmnopqrstuvwxyz'
    RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def get_alphabet(language_characters: LanguageCharacters) -> str:
    return language_characters.value + string.digits


def check_language_identity(text: str, checkable_language_characters: LanguageCharacters) -> bool:
    for language_characters in LanguageCharacters:
        if language_characters != checkable_language_characters and set(text) & set(language_characters.value):
            return False
    return True
