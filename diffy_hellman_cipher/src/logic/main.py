import random
import math


def calculate_jacobian(a, n):  # Вычиляем Якобиан по его свойствам
    if a == 0:
        return 0
    ans = 1  

    if a < 0:
        a = -a  
        if n % 4 == 3:
            ans = -ans  

    if a == 1:
        return ans 
  
    while a:
        if a < 0:
            a = -a
            if n % 4 == 3:
                ans = -ans

        while a % 2 == 0:
            a = a // 2
            if n % 8 == 3 or n % 8 == 5:
                ans = -ans 

        a, n = n, a
  
        if a % 4 == 3 and n % 4 == 3:
            ans = -ans
        a = a % n
  
        if a > n // 2:
            a = a - n
  
    if n == 1:
        return ans
  
    return 0


def solovay_strassen(p):
    if p % 2 == 0:
        return False
  
    for i in range(math.ceil(math.log2(p))): # каждую итерацию вероятность получить ошибку = 1/2^k k = 1, 2, 3, 4, ...
        a = random.randint(1, p - 1) # берем рандомное число
        jacobian = (p + calculate_jacobian(a, p)) % p # вычисляем Якобиан
        mod = pow(a, (p - 1) // 2, p)
        if jacobian == 0 or mod != jacobian:  # если условия не выполняются, то число составное
            return False

    return True


#получаем число Софи Жермен (Оно выполняет след условия:
# оно простое
# p*2 + 1 также простое
# )
def get_sg(bit: int):
    while True:
        prime = get_prime(bit)
        if solovay_strassen(prime * 2 + 1):
            return prime
        

# получаем первообразный корень 
# Функция принимает битность числа и число Софи Жермен
# В функции проверяем условия первообразного корня числа 
#сслыка на свойства https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B2%D0%BE%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BE%D1%80%D0%B5%D0%BD%D1%8C_(%D1%82%D0%B5%D0%BE%D1%80%D0%B8%D1%8F_%D1%87%D0%B8%D1%81%D0%B5%D0%BB)
def get_primitive_root(bit: int, p: int):
    while True:
        g = random.randint(2**bit, 2**(bit + 1) - 1)
        if math.gcd(g, p) == 1:
            if pow(g, (p - 1) // 2, p) != 1:
                if pow(g, 2, p) != 1:
                    return g


def get_prime(bit: int):
    while True:
        a = random.randint(2**bit, 2**(bit + 1) - 1)
        if solovay_strassen(a):
            return a

