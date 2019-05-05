from itertools import product, chain
S = input()
num = 0
for plus in product(("", "+"), repeat=len(S) - 1):
    num += eval("".join(chain.from_iterable(zip(S, list(plus) + [""]))))
print(num)
