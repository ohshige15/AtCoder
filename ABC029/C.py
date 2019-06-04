import itertools
N = int(input())
for s in itertools.product(("a", "b", "c"), repeat=N):
    print("".join(s))
