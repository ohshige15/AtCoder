N = input()
num = 0
for i, n in enumerate(N):
    left = int(N[:i]) if i != 0 else 0
    right = int(N[i + 1:]) if i != len(N) - 1 else 0
    if 1 < int(n):
        num += 10 ** (len(N) - i - 1) * (left + 1)
    elif 1 == int(n):
        num += 10 ** (len(N) - i - 1) * left + right + 1
    else:
        num += 10 ** (len(N) - i - 1) * left
print(num)
