S = list(input())
N = int(input())
for _ in range(N):
    l, r = map(int, input().split())
    s = list(reversed(S[l-1:r]))
    S = S[:l-1] + s + S[r:]
print("".join(S))
