from dataclasses import dataclass


@dataclass
class RSAPublicKey:
    e: int
    n: int


@dataclass
class RSAPrivateKey:
    d: int
    n: int


@dataclass
class RSAKeyGeneration:
    public_key: RSAPublicKey
    private_key: RSAPrivateKey
    p: int
    q: int
    euler: int
