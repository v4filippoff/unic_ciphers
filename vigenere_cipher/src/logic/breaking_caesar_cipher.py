from collections import Counter

from src.logic.dto import BreakCipherResult
from src.logic.language_characters import LanguageCharacters, check_language_identity, MOST_COMMON_EN, MOST_COMMON_RU


def get_text_language_characters(text: str) -> LanguageCharacters:
    normalized_text = text.lower()
    for language_characters in LanguageCharacters:
        if check_language_identity(normalized_text, language_characters):
            return language_characters
    raise ValueError("Символы текста должны быть из одного алфавита.")


def break_cipher(text: str) -> BreakCipherResult:
    language_characters = get_text_language_characters(text)
    alphabet: str = language_characters.value

    text_characters_counter = Counter(text)
    text_most_common_character = ''
    for counter_item in text_characters_counter.most_common():
        if counter_item[0] in alphabet:
            text_most_common_character = counter_item[0]
            break

    alphabet_most_common_character: str = ''
    if language_characters == LanguageCharacters.EN:
        alphabet_most_common_character = MOST_COMMON_EN
    elif language_characters == LanguageCharacters.RU:
        alphabet_most_common_character = MOST_COMMON_RU

    if not text_most_common_character:
        key = 0
    else:
        key = alphabet.find(text_most_common_character) - alphabet.find(alphabet_most_common_character)

    characters_map = {char: alphabet[(current_index - key) % len(alphabet)] for current_index, char in enumerate(alphabet)}
    decrypted_text = ''
    for char in text:
        if char.lower() in alphabet:
            if char.islower():
                decrypted_text += characters_map[char]
            else:
                decrypted_text += characters_map[char.lower()].upper()
        else:
            decrypted_text += char

    return BreakCipherResult(key=key, decrypted_text=decrypted_text)
