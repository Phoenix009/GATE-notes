from math import factorial

def helper1(n):
    if n%2 or n == 0: return 0
    return n-1 + helper1(n-2)

def helper2(n):
    if n%2: return 0
    n >>= 1
    return factorial(2*n)//(factorial(n) * (2**n))

n = int(input())
print(helper1(n), helper2(n))
