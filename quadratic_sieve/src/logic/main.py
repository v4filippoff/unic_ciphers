from math import sqrt, gcd, log, exp
import numpy as np
from sympy import isprime


class QS:

    def __init__(self, factorizal_number: int, B_prime: int, A: int) -> None:
        self.factorizal_number = factorizal_number
        self.sqrt_factorizal_number = int(sqrt(factorizal_number)) + 1
        self.B_prime = B_prime
        self.A = A
        self.prime_quadratic_resudies = list()
        self.values_Q = list()
        self.index_values_Q = list()
        self.get_values_Q()
        self.get_quadratic_resudies()
        self.matrix = None  # np.zeros((len(self.values_Q), len(self.prime_quadratic_resudies)), dtype=np.dtype('b'))
        self.get_matrix()
        self.dependent_vectors = list()
        self.independent_vectors = list()
        self.solve_dict = dict()
        self.get_dependent_independent_vectors()

    def get_quadratic_resudies(self):
        self.prime_quadratic_resudies.append(2)
        for i in range(3, self.B_prime, 2):
            if isprime(i) and pow(self.factorizal_number, (i - 1) // 2, i) == 1:
                self.prime_quadratic_resudies.append(i)
        print('get_quadratic_resudies - done!')

    def get_values_Q(self):
        for i in range(self.A):
            self.values_Q.append((self.sqrt_factorizal_number + i) ** 2 - self.factorizal_number)
        print('get_values_Q - done!')

    # (n +i) ** 2 - n

    # def get_matrix(self):
    #     temp_matrix = [([False] * len(self.prime_quadratic_resudies)) for i in range(len(self.values_Q))]
    #     temp_value = self.values_Q[:]
    #     print('Complete')
    #     for i_value_Q, value_Q in enumerate(temp_value):
    #         for i_prime, prime in enumerate(self.prime_quadratic_resudies):
    #             while temp_value[i_value_Q] % prime == 0:
    #                 temp_matrix[i_value_Q][i_prime] ^= True
    #                 temp_value[i_value_Q] //= prime

    #     self.index_values_Q = [self.sqrt_factorizal_number + i for i, v in enumerate(temp_value) if v == 1]
    #     self.values_Q = [self.values_Q[i] for i, v in enumerate(temp_value) if v == 1]
    #     self.matrix = np.array([temp_matrix[i] for i, v in enumerate(temp_value) if v == 1], dtype=np.dtype('b'))
    #     print('get_matrix - complete')

    def get_matrix(self):
        temp_value = self.values_Q[:]
        help_matrix = []
        temp_index_values_Q = []
        temp_values_Q = []
        print('Complete')
        for i_value_Q, value_Q in enumerate(temp_value):
            temp_matrix = [False] * len(self.prime_quadratic_resudies)
            for i_prime, prime in enumerate(self.prime_quadratic_resudies):
                while temp_value[i_value_Q] % prime == 0:
                    temp_matrix[i_prime] ^= True
                    temp_value[i_value_Q] //= prime
            if temp_value[i_value_Q] == 1:
                print(i_value_Q)
                temp_index_values_Q.append(self.sqrt_factorizal_number + i_value_Q)
                temp_values_Q.append(self.values_Q[i_value_Q])
                help_matrix.append(temp_matrix)
        self.index_values_Q = temp_index_values_Q
        self.values_Q = temp_values_Q
        self.matrix = np.array(help_matrix, dtype=np.dtype('b'))
        # return self.matrix = np.array([temp_matrix[i] for i, v in enumerate(temp_value) if v == 1], dtype=np.dtype('b'))

    # def get_matrix(self):
    #     n = len(self.values_Q)//2

    #     for i in range(2):
    #     temp_matrix = [([False] * len(self.prime_quadratic_resudies)) for i in range(len(self.values_Q))]
    #     temp_value = self.values_Q[:]
    #     print('Complete')
    #     for i_value_Q, value_Q in enumerate(temp_value):
    #         for i_prime, prime in enumerate(self.prime_quadratic_resudies):
    #             while temp_value[i_value_Q] % prime == 0:
    #                 temp_matrix[i_value_Q][i_prime] ^= True
    #                 temp_value[i_value_Q] //= prime

    #     self.index_values_Q = [self.sqrt_factorizal_number + i for i, v in enumerate(temp_value) if v == 1]
    #     self.values_Q = [self.values_Q[i] for i, v in enumerate(temp_value) if v == 1]
    #     self.matrix = np.array([temp_matrix[i] for i, v in enumerate(temp_value) if v == 1], dtype=np.dtype('b'))
    #     print('get_matrix - complete')

    def xor_column(self, column_index: int, row_index: int):
        for i in range(len(self.matrix[0])):
            if i != column_index and self.matrix[row_index, i] == 1:
                self.matrix[:, i] ^= self.matrix[:, column_index]

    def get_dependent_independent_vectors(self):
        print('get_dependent_independent_vectors')
        print(f'{len(self.matrix)} -- shape')
        print(f'{len(self.matrix[0])} -- shape')
        for i_column in range(len(self.matrix[0])):
            for i_row in range(len(self.matrix)):
                if self.matrix[i_row, i_column] == 1:
                    self.independent_vectors.append(i_row)
                    self.solve_dict[i_column] = i_row
                    self.xor_column(i_column, i_row)
                    break

        self.dependent_vectors = [i for i in range(len(self.matrix)) if i not in self.independent_vectors]

    def solve(self):
        print('Start solving matrix')
        for dependent_vector in self.dependent_vectors:
            quadratic_indexes = self.index_values_Q[dependent_vector]
            mult_values_Q = self.values_Q[dependent_vector]
            for ind, val in enumerate(self.matrix[dependent_vector]):
                if val == 1:
                    quadratic_indexes *= self.index_values_Q[self.solve_dict[ind]]
                    mult_values_Q *= self.values_Q[ind]

            try:
                if gcd(quadratic_indexes - int(sqrt(mult_values_Q)), self.factorizal_number) != 1 and gcd(
                        quadratic_indexes - int(sqrt(mult_values_Q)), self.factorizal_number) != self.factorizal_number:
                    return gcd(quadratic_indexes - int(sqrt(mult_values_Q)), self.factorizal_number)
            except ValueError:
                pass


if __name__ == '__main__':
    n = 344572667627327574872986520507
    # n = 1208926595608279142148049
    # n = 1099511980717 * 1099511980597
    # n = 11023530013 #Test
    # n = 2954945083
    # n = 945143891
    # n = 15347
    # n = 14821 * 14939
    a = exp(sqrt(log(n) * log(log(n))))
    # print(a)
    # print(int(a))
    qs = QS(n, 10 ** 5, 200000)
    # qs = QS(n, 10**2, 60000)
    # print(qs.values_Q)
    # print(qs.solve())
    a = qs.solve()
    print(a)
    print(n // a)

