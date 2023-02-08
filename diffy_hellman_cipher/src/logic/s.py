from math import sqrt, ceil
# Алгоритм Гельфонда Шэнкса https://ru.m.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%93%D0%B5%D0%BB%D1%8C%D1%84%D0%BE%D0%BD%D0%B4%D0%B0_%E2%80%94_%D0%A8%D0%B5%D0%BD%D0%BA%D1%81%D0%B0


# Функция больших шагов
def get_giant_step(g, p, a):
    res = []
    m = int(sqrt(p)) + 1
    for i in range(1, m + 1):
        res.append(pow(g, i * m, p)) # создаем массив больших шагов где res[i] = g**(i * (sqrt(p) + 1)) mod p
    return res


# Функция малых шагов
def get_baby_step(g, p, a):
    res = []
    m = int(sqrt(p)) + 1
    for i in range(1, m + 1):
        res.append(a * (pow(g, i, p))%p) # создаем массив малых шагов где res[i] = a * g**i  mod p
    return res


def gelfond_shanks(g, p, a):
    giant = get_giant_step(g, p, a)
    print('Giant complete')
    baby = get_baby_step(g, p, a)
    print('Baby complete')
    m = int(sqrt(p)) + 1
    for i, v in enumerate(giant):
        if v in baby:
            return m * (i + 1) - baby.index(v) - 1 # находим значение по формуле: (sqrt(m) + 1) * i - j, где i и j индексы одинаковых значений в списках 
