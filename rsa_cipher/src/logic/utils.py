ENCODING = 'cp1251'


def convert_str_to_int(text: str) -> int:
    bit_string = '1' + ''.join('{0:08b}'.format(s) for s in text.encode(ENCODING))
    return int(bit_string, base=2)


def convert_int_to_str(number: int) -> str:
    number_bits = '{0:08b}'.format(number)[1:]
    result = ''
    for i in range(0, len(number_bits), 8):
        try:
            result += int(number_bits[i:i+8], base=2).to_bytes(1).decode(ENCODING)
        except UnicodeDecodeError:
            result += '\0'
    return result


if __name__ == '__main__':
    number = convert_str_to_int('dfgfjei564w85#$*$*%&@($*#T$')
    print(number)
    message = convert_int_to_str(number)
    print(message)
