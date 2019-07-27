A, B = map(int, input().split())
K = A + B
if K % 2 != 0:
    print("IMPOSSIBLE")
else:
    print(K // 2)
