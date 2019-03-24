S = input()
n = 0
result = 0
for s in S:
    if s in ("A", "C", "G", "T"):
        n += 1
    else:
        result = max(result, n)
        n = 0
result = max(result, n)
print(result)
