import enum
import string

MOST_COMMON_EN = 'e'
MOST_COMMON_RU = 'о'
HIT_INDEX_EN = 0.0644
HIT_INDEX_RU = 0.0553


class LanguageCharacters(enum.Enum):
    EN = 'abcdefghijklmnopqrstuvwxyz'
    RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def get_alphabet(language_characters: LanguageCharacters) -> str:
    return language_characters.value


def check_language_identity(text: str, checkable_language_characters: LanguageCharacters) -> bool:
    for language_characters in LanguageCharacters:
        if language_characters != checkable_language_characters and set(text) & set(language_characters.value):
            return False
    return True


def get_text_language_characters(text: str) -> LanguageCharacters:
    normalized_text = text.lower()
    for language_characters in LanguageCharacters:
        if check_language_identity(normalized_text, language_characters):
            return language_characters
    raise ValueError("Символы текста должны быть из одного алфавита.")
