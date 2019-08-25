from collections import Counter
S = Counter(input())
for s, n in S.most_common():
    if n != 2:
        print("No")
        exit()
print("Yes")
