from dataclasses import dataclass


@dataclass
class BreakCipherResult:
    key: int
    decrypted_text: str
