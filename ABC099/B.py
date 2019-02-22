a, b = map(int, input().split())
diff = b - a
B = sum(range(1, diff + 1))
print(B - b)
