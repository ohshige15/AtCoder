from collections import Counter
S = Counter(input())
print(" ".join([str(S[s]) for s in ("A", "B", "C", "D", "E", "F")]))
