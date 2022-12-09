from collections import Counter

from src.logic.language_characters import get_text_language_characters, LanguageCharacters, MOST_COMMON_EN, \
    MOST_COMMON_RU


def break_caesar_cipher(text: str) -> int:
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

    return key
