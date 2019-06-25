N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))
if len(P) != len(set(P)):
    print("NO")
    exit()
if a in P or b in P:
    print("NO")
    exit()
print("YES")
