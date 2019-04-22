from collections import Counter
N = int(input())
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
num = Counter()
for n in range(1, N + 1):
    factors = prime_factors(n)
    num.update(factors)
x = 1
for _, n in num.items():
    x *= (n + 1)
    x %= 10 ** 9 + 7
print(x)
