def calculateJacobian(a, n):  # Вычиляем Якобиан по его свойствам
    if (a == 0):  
        return 0
    ans = 1  

    if (a < 0):  
        a = -a  
        if (n % 4 == 3):  
            ans = -ans  

    if (a == 1):  
        return ans 
  
    while (a):  
        if (a < 0): 
            a = -a;  
            if (n % 4 == 3): 
                ans = -ans

        while (a % 2 == 0):  
            a = a // 2;  
            if (n % 8 == 3 or n % 8 == 5):  
                ans = -ans 

        a, n = n, a;  
  
        if (a % 4 == 3 and n % 4 == 3):  
            ans = -ans
        a = a % n
  
        if (a > n // 2):  
            a = a - n
  
    if (n == 1):  
        return ans
  
    return 0
  
def solovayStrassen(p, iterations):  
  
    if (p < 2):  
        return False
    if (p != 2 and p % 2 == 0):  #четно ли число
        return False
  
    for i in range(iterations): # каждую итерацию вероятность получить ошибку = 1/2^k k = 1, 2, 3, 4, ...
          
        a = random.randint(1, p - 1) # берем рандомное число
        jacobian = (p + calculateJacobian(a, p)) % p # вычисляес Якобиан
        mod = pow(a, (p - 1) // 2, p)
  
        if (jacobian == 0 or mod != jacobian):  # если условия не выполняются, то число составное
            return False
  
    return True


import random   
import math
import sympy 


#получаем число Софи Жермен (Оно выполняет след условия:
# оно простое
# p*2 + 1 также простое
# )
def get_SG(bit: int):
    while True:
        prime = random.randint(2**(bit - 1), 2**(bit) - 1)
        if solovayStrassen(prime, 5) and solovayStrassen(prime * 2 + 1, 5):
            return prime
        

# получаем первообразный корень 
# Функция принимает битность числа и число Софи Жермен
# В функции проверяем условия первообразного корня числа 
#сслыка на свойства https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B2%D0%BE%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BE%D1%80%D0%B5%D0%BD%D1%8C_(%D1%82%D0%B5%D0%BE%D1%80%D0%B8%D1%8F_%D1%87%D0%B8%D1%81%D0%B5%D0%BB)
def PrimitiveRoot(bit: int, p_sg: int):
    p = 2 * p_sg + 1
    while True:
        g = random.randint(2**bit, 2**(bit+1)- 1)
        if math.gcd(p, g):# первое условие
            if pow(g, (p-1)//2, p) != 1 :# второе условие
                if pow(g, 2, p) != 1 and pow(g, p_sg, p) != 1:# третье условие
                    return g


#получение простого числа
def get_prime(bit: int):
    while True:
        a = random.randint(2**bit, 2**(bit + 1) - 1)#получаем рандомное определенной битности
        if solovayStrassen(a, 5):#проверяем на простоту, если проходит, то возвращаем число
            return a

