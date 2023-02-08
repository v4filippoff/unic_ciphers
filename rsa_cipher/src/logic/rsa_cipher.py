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
    if number % 2 == 0:
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


def get_prime(nbits: int) -> int:
    while True:
        a = random.randint(2 ** nbits, 2 ** (nbits + 1) - 1)
        if is_number_prime(a):
            return a


def generate_keys(nbits: int) -> RSAKeyGeneration:
    p, q = get_prime(nbits), get_prime(nbits)
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
