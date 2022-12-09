from dataclasses import dataclass


@dataclass
class BreakCipherResult:
    key: str
    decrypted_text: str
