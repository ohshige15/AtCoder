S = input()
K = int(input())
for i, s in enumerate(S):
    if s != "1":
        print(s)
        break
    if i + 1 >= K:
        print(s)
        break
