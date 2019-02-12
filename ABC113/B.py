input()
T, A = map(int, input().split())
H = list(map(int, input().split()))
d = None
x = None
for i, h in enumerate(H):
    a = T - h * 0.006
    if d is None or d > abs(A - a):
        d = abs(A - a)
        x = i + 1
print(x)
