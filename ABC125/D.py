N = int(input())
A = list(map(int, input().split()))
B = [abs(a) for a in A]
M = len([a for a in A if a < 0])
if M % 2 == 0:
    print(sum(B))
else:
    print(sum(B) - 2 * min(B))
