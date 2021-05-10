import math
import numpy as np
from typing import List, Dict
import numpy.typing as npt

def get_group_generators(p) -> List[int]:
    """
    Is the size of the group which is all number below p
    which is relative prime with p
    """
    return  list(filter(lambda x: math.gcd(x, p) == 1, range(p)))

def is_generator_of(n: int, p: int) -> bool:
    """
    A generator must have order p-1 when the modululus is p.
    To check this we only have to check 2**(p-1) / f mod p != 1
    for the prime factors f of p-1.
    Example:
    g=3, p=43
    factors of p-1 = 2*3*6
    2*3 = 6
    2*7 = 14
    3*7 = 21
    Need to check that all muliplicatives of factors g**(6,14,21)
    % 43 != 1
    """
    group = get_group_generators(p)
    generators = list(map(lambda i:
        n**i % p, group
        ))
    print(f"Zp: {group}")
    print(f"Generators sorted: {sorted(generators)}")
    print(f"Generators listed: {(generators)}")
    return set(group )== set(generators)

def phi(n: int) -> int: return len(get_group_generators(n))

def get_inverse_modulo(a: int, n: int) -> int:
    return pow(a, -1, n)

def square_and_multiply(exponent: int) -> Dict[str, int]:
    # Remove byte prefix
    byteString = binary(exponent)[2:]
    print(f"ByteString {byteString}")

    # Squares are length of byteString - 1
    # multiples are number of 1¨s -1
    squaresAndMultiplies = {"square": 0, "multiplies": 0}
    squaresAndMultiplies["multiplies"] = byteString.count("1") - 1
    squaresAndMultiplies["square"] = len(byteString) -1

    print(squaresAndMultiplies)
    return square_and_multiply

def binary(number: int) -> str: return bin(number)

def find_discrete_logarithm(generator: int, modulo: int, x) -> int:
    for i in range(x):
        if generator ** i % modulo == x:
            print(f"{generator}^{i} mod {modulo} = {x}")
            return i

def encrypt_hill_cipher(
        key: npt.ArrayLike,
        plaintext: npt.ArrayLike,
        mod: int,
        ) -> npt.ArrayLike:
    """
    Key and plaintext are matrixes
    Made by regular python double lists
    02
    13
    [[0,2], [1,3]]
    """
    return np.dot(key, plaintext) % mod


def hill_cipher_find_k_inverse(key: npt.ArrayLike, n: int) -> npt.ArrayLike:
    """
    42
    22
    K = [[4,2], [2,2]]
    """
    determinant = (key[0][0]*key[1][1] - key[0][1]*key[1][0])
    print(f"Determinant: {determinant}^-1")
    determinant_inverse = get_inverse_modulo(int(determinant), n)
    print(f"Determinant inverse: {determinant_inverse}")
    key[0][0], key[1][1] = key[1][1], key[0][0]
    key[0][1], key[1][0] = n -key[0][1], n -key[1][0]
    print(f"new key: {key}")
    key_inverse = determinant_inverse * key % 5
    print(f"K^-1: {key_inverse}")
    return key_inverse
