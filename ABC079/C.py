from itertools import product
A, B, C, D = list(input())
for op1, op2, op3 in product(("+", "-"), repeat=3):
    e = A + op1 + B + op2 + C + op3 + D
    x = eval(e)
    if x == 7:
        print(e + "=7")
        break
