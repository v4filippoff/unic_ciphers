from typing import List, Tuple

from src.logic.language_characters import LanguageCharacters, get_alphabet


def are_text_and_key_from_same_alphabet(text: str, key: str) -> bool:
    if (set(text) & set(LanguageCharacters.EN.value)) and (set(key) & set(LanguageCharacters.RU.value)) or \
            (set(text) & set(LanguageCharacters.RU.value)) and (set(key) & set(LanguageCharacters.EN.value)):
        return False
    return True


def get_text_characters_caesar_key_items(text: str, key: str, alphabet: str) -> List[Tuple[str, int]]:
    caesar_keys = []
    for key_character in key:
        caesar_keys.append(alphabet.find(key_character))

    text_characters_caesar_key_items = []
    for i in range(len(text)):
        character_key_item = (text[i], caesar_keys[i % len(caesar_keys)])
        text_characters_caesar_key_items.append(character_key_item)

    return text_characters_caesar_key_items


def encrypt(text: str, key: str, language_characters: LanguageCharacters) -> str:
    alphabet = get_alphabet(language_characters)
    text_characters_caesar_key_items = get_text_characters_caesar_key_items(text, key, alphabet)

    encrypted_text = ''
    for text_character, caesar_key in text_characters_caesar_key_items:
        alphabet_index = alphabet.find(text_character)
        if alphabet_index != -1:
            encrypted_text += alphabet[(alphabet_index + caesar_key) % len(alphabet)]
        else:
            encrypted_text += text_character

    return encrypted_text


def decrypt(text: str, key: str, language_characters: LanguageCharacters) -> str:
    alphabet = get_alphabet(language_characters)
    text_characters_caesar_key_items = get_text_characters_caesar_key_items(text, key, alphabet)

    decrypted_text = ''
    for text_character, caesar_key in text_characters_caesar_key_items:
        alphabet_index = alphabet.find(text_character)
        if alphabet_index != -1:
            decrypted_text += alphabet[(alphabet_index - caesar_key) % len(alphabet)]
        else:
            decrypted_text += text_character

    return decrypted_text
