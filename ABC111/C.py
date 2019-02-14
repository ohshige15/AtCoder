from collections import Counter
input()
V = list(map(int, input().split()))
odd = Counter(V[::2])
even = Counter(V[1::2])
odd_max = max(odd.items(), key=lambda x: x[1])
even_max = max(even.items(), key=lambda x: x[1])
if odd_max[0] != even_max[0]:
    print(len(V) - odd_max[1] - even_max[1])
    exit()
odd_second = odd.most_common(2)
if len(odd_second) >= 2:
    odd_second = odd_second[1][1]
else:
    odd_second = 0
even_second = even.most_common(2)
if len(even_second) >= 2:
    even_second = even_second[1][1]
else:
    even_second = 0
if odd_second >= even_second:
    first = even_max[1]
    second = odd_second
else:
    first = odd_max[1]
    second = even_second
print(len(V) - first - second)
