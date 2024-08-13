#!/usr/bin/env python3
import math
from typing import List, Set, Dict, Tuple


def findDivisors(num: int) -> List[int]:
    divisors = []
    for div in range(1, int(math.sqrt(num))+1):
        if num % div == 0:
            divisors.append(div)
    return divisors


def slowIsPrime(num: int) -> bool:
    if num < 2:
        return False
    divisors = findDivisors(num)
    if len(divisors) == 1:
        return True


def uniqueFactorization(num: int) -> List[int]:
    factors = []
    for fac in range(2, num):
        if num == 1:
            break
        if slowIsPrime(fac):
            while num % fac == 0:
                num //= fac
                factors.append(fac)
    return factors


if __name__ == '__main__':
    while True:
        a = int(input())
        print(uniqueFactorization(a))
