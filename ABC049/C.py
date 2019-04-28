S = input()
while True:
    for t in ("dream", "dreamer", "erase", "eraser"):
        if S.endswith(t):
            S = S[:-len(t)]
            break
    else:
        print("NO")
        exit()
    if S == "":
        print("YES")
        break
