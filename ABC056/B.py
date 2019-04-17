W, a, b = map(int, input().split())
if a < b:
    print(max(b - (a + W), 0))
else:
    print(max(a - (b + W), 0))
