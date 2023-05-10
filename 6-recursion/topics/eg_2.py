''' Question: Calculate n raised to power p. '''

import math
from math import pow

def power(n, p):
    if p == 0:
        return 1

    pre_pow = power(n, p-1)
    return n * pre_pow

n = int(input("Enter the number: "))
p = int(input("Enter the power: "))
print("The answer: ", int(power(n,p)))