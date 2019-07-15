N = int(input())
s = N % 60
N //= 60
m = N % 60
N //= 60
print("{0:02d}:{1:02d}:{2:02d}".format(N, m, s))
