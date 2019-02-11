S = input()
a = 100000
for i in range(len(S) - 2):
    s = int(S[i:i + 3])
    a = min(a, abs(753 - s))
print(a)
