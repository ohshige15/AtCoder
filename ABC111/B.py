N = input()
x = N[0] * len(N)
if int(x) >= int(N):
    print(x)
    exit()
x = str(int(N[0]) + 1) * len(N)
print(x)
