import enum
import string


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


def encrypt(text: str, key: int, language_characters: LanguageCharacters) -> str:
    alphabet = get_alphabet(language_characters)

    encrypted_text = ''
    for text_character in text:
        alphabet_index = alphabet.find(text_character)
        if alphabet_index != -1:
            encrypted_text += alphabet[(alphabet_index + key) % len(alphabet)]
        else:
            encrypted_text += text_character

    return encrypted_text


def decrypt(text: str, key: int, language_characters: LanguageCharacters) -> str:
    alphabet = get_alphabet(language_characters)

    decrypted_text = ''
    for text_character in text:
        alphabet_index = alphabet.find(text_character)
        if alphabet_index != -1:
            decrypted_text += alphabet[(alphabet_index - key) % len(alphabet)]
        else:
            decrypted_text += text_character

    return decrypted_text
