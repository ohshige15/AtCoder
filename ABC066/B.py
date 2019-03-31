S = input()
for i in range(len(S) - 1, 1, -1):
    if i % 2 != 0:
        continue
    for j in range(len(S[:i]) // 2):
        if S[j] != S[i // 2 + j]:
            break
    else:
        print(i)
        exit()
