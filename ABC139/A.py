S = input()
T = input()
num = 0
for s, t in zip(S, T):
    if s == t:
        num += 1
print(num)
