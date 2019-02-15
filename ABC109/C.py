from fractions import gcd
from functools import reduce
N, X = map(int, input().split())
x_list = list(map(int, input().split()))
x_list.append(X)
x_list.sort()
diff_list = [x_list[i + 1] - x_list[i] for i in range(len(x_list) - 1)]
print(reduce(gcd, diff_list))
