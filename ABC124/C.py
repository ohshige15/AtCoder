S = input()
L1 = "".join(["1" if i % 2 == 0 else "0" for i in range(len(S))])
L2 = "".join(["0" if i % 2 == 0 else "1" for i in range(len(S))])
num1 = sum([1 if s != l else 0 for s, l in zip(S, L1)])
num2 = sum([1 if s != l else 0 for s, l in zip(S, L2)])
print(min(num1, num2))
