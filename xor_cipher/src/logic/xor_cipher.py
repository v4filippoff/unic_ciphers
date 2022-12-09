from bitarray import bitarray
import random


ENCODING = 'cp1251'
BITS_IN_BYTE = 8


def generate_random_key(length: int) -> str:
    random_digits = [random.randint(0, 1) for _ in range(length)]
    indexes_0 = set()
    indexes_1 = set()
    for i, digit in enumerate(random_digits):
        if digit:
            indexes_1.add(i)
        else:
            indexes_0.add(i)

    indexes_for_choice = indexes_1 if len(indexes_1) > len(indexes_0) else indexes_0
    for _ in range(abs(len(indexes_1) - len(indexes_0)) // 2):
        current_index = random.choice(list(indexes_for_choice))
        indexes_for_choice.remove(current_index)
        random_digits[current_index] = int(not random_digits[current_index])

    return ''.join(map(str, random_digits))


def convert_str_to_binary_string(text: str) -> str:
    ba = bitarray()
    ba.frombytes(text.encode(ENCODING))
    return ba.to01()


def convert_binary_string_to_str(binary_string: str) -> str:
    ba = bitarray(binary_string)
    return ba.tobytes().decode(ENCODING)


def normalize_key(text: str, key: str) -> str:
    text_length = len(text)
    key_length = len(key)
    if text_length > key_length:
        for current_index in range(key_length, text_length, key_length):
            key += key if current_index + key_length <= text_length else key[:text_length - current_index]
    elif text_length < key_length:
        return key[:text_length]
    return key


def apply_xor(text: str, key: str) -> str:
    binary_text = convert_str_to_binary_string(text)
    key = normalize_key(binary_text, key)
    return ''.join(str(int(binary_text[i]) ^ int(key[i])) for i in range(len(binary_text)))
