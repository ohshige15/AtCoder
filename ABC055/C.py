S, C = map(int, input().split())
if S >= C // 2:
    print(C // 2)
    exit()
C -= 2 * S
print(S + C // 4)
