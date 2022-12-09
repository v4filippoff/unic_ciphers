from collections import Counter

from src.logic import vigenere_cipher
from src.logic.breaking_caesar_cipher import break_caesar_cipher
from src.logic.dto import BreakCipherResult
from src.logic.exceptions import KeyLengthNotFound, NotOnlyAlphabetCharactersError
from src.logic.language_characters import get_text_language_characters, HIT_INDEX_EN, LanguageCharacters, HIT_INDEX_RU


def calculate_hit_index(alphabet: str, text: str) -> float:
    if len(text) <= 1:
        return 0
    alphabet_char_counter = Counter(text)
    hit_index = 0
    for char in alphabet:
        if not alphabet_char_counter[char]:
            continue
        hit_index += (alphabet_char_counter[char] * (alphabet_char_counter[char] - 1)) / (len(text) * (len(text) - 1))
    return hit_index


def find_key_length(alphabet: str, text: str, expected_hit_index: float) -> int:
    eps = 0.005
    for expected_key_length in range(1, len(text) // 2):
        hit_indexes: set[float] = set()
        for offset in range(expected_key_length):
            current_group = text[offset::expected_key_length]
            hit_indexes.add(calculate_hit_index(alphabet, current_group))
        average_hit_index = sum(hit_indexes) / len(hit_indexes)
        if abs(average_hit_index - expected_hit_index) < eps:
            return expected_key_length


def break_vigenere_cipher(text: str) -> BreakCipherResult:
    text = text.lower().strip()
    language_characters = get_text_language_characters(text)
    alphabet: str = language_characters.value

    if set(text) - set(alphabet):
        raise NotOnlyAlphabetCharactersError()

    expected_hit_index = HIT_INDEX_EN if language_characters == LanguageCharacters.EN else HIT_INDEX_RU
    key_length = find_key_length(alphabet, text, expected_hit_index)
    if key_length is None:
        raise KeyLengthNotFound()
    key = ''
    for offset in range(key_length):
        caesar_key = break_caesar_cipher(text[offset::key_length])
        key += alphabet[caesar_key]
    decrypted_text = vigenere_cipher.decrypt(text, key, language_characters)
    return BreakCipherResult(key=key, decrypted_text=decrypted_text)


# with open('../text.txt', 'r') as f:
#     text = f.read()
# print(break_vigenere_cipher(text))
