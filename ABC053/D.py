from collections import Counter
N = int(input())
A = Counter(list(map(int, input().split()))).items()
rest = len([a for a, n in A if n % 2 == 0])
if rest % 2 == 1:
    print(len(A) - 1)
    exit()
print(len(A))
