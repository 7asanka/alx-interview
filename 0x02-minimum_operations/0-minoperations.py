#!/usr/bin/python3
"""
minimum operations module
"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed
    to get exactly n 'H' characters using Copy All and Paste.
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

