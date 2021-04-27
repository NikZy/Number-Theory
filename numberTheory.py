import math

def get_group_generators(p) -> List[int]:
    """
    Is the size of the group which is all number below p
    which is relative prime with p
    """
    return  list(filter(lambda x: math.gcd(x, p) == 1, range(p)))


def get_inverse_modulo(a, n) -> int:
    return pow(a, -1, n)
