import math
import random

from src.logic.dto import RSAKeyGeneration, RSAPublicKey, RSAPrivateKey
from src.logic.exceptions import TooBigMessage
from src.logic.utils import convert_str_to_int, convert_int_to_str


def fast_pow_mod(base: int, exp: int, mod: int) -> int:
    result = 1
    while exp:
        if exp & 1:
            result *= base
            result %= mod
        base *= base
        base %= mod
        exp >>= 1
    return result


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def is_number_prime(number: int) -> bool:
    # Проверяем делимость на маленькие простые числа до определенного предела
    small_prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251]
    if number in small_prime_numbers:
        return True
    for small_prime in small_prime_numbers:
        if number % small_prime == 0:
            return False

    # Тест Миллера-Рабина
    s, d = 1, (number - 1) // 2
    while 2 ** s <= number - 1:
        if ((number - 1) % 2 ** s == 0) and ((number - 1) // 2 ** s % 2 == 1):
            d = number // 2 ** s
            break
        s += 1

    rounds = math.ceil(math.log2(number))
    for _ in range(rounds):
        a = random.randint(2, number - 1)
        if fast_pow_mod(a, d, number) == 1:
            continue
        for r in range(s):
            if fast_pow_mod(a, (2 ** r) * d, number) == number - 1:
                break
        else:
            return False
    return True


def generate_prime_number(nbits: int) -> int:
    random_bits = '1' + ''.join(random.choice(['0', '1']) for _ in range(nbits - 1))
    current_random_number = int(random_bits, 2)
    current_random_number += not(current_random_number % 2)
    while not is_number_prime(current_random_number):
        current_random_number += 2
    return current_random_number


def generate_keys(nbits: int) -> RSAKeyGeneration:
    p, q = generate_prime_number(nbits), generate_prime_number(nbits)
    n = p * q
    euler = (p - 1) * (q - 1)
    e = 65537

    get_positive_d = lambda d: (d if d > 0 else euler * math.ceil(abs(d) / euler) + d)
    return RSAKeyGeneration(
        public_key=RSAPublicKey(e=e, n=n),
        private_key=RSAPrivateKey(d=get_positive_d(extended_gcd(e, euler)[1]), n=n),
        p=p, q=q, euler=euler
    )


def encrypt(text: str, public_key: RSAPublicKey) -> int:
    text_int = convert_str_to_int(text)
    if text_int >= public_key.n:
        raise TooBigMessage('Слишком большое сообщение!')
    return fast_pow_mod(text_int, public_key.e, public_key.n)


def decrypt(text_int: int, private_key: RSAPrivateKey) -> str:
    if text_int >= private_key.n:
        raise TooBigMessage('Слишком большое сообщение!')
    result_int = fast_pow_mod(text_int, private_key.d, private_key.n)
    return convert_int_to_str(result_int)


if __name__ == '__main__':
    key_generation = generate_keys(512)
    encrypted = encrypt('Привет Как дела у543!', key_generation.public_key)
    print(encrypted)
    decrypted = decrypt(encrypted, key_generation.private_key)
    print(decrypted)
