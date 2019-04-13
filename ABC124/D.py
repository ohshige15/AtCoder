N, K = map(int, input().split())
S = input()
if S == "0":
    print(1)
    exit()
if S.count("0") == N:
    print(N)
    exit()
L = [0]
prev = S[0]
num = 1
for s in S[1:]:
    if s == prev:
        num += 1
    else:
        L.append(num)
        num = 1
        prev = s
L.append(num)
# print(L)
for i in range(1, len(L)):
    L[i] += L[i - 1]
# print(L)
left = 0
if S[0] == "1":
    right = min(2 * K + 1, len(L) - 1)
else:
    right = min(2 * K, len(L) - 1)
num = 0
while right < len(L):
    # print("L[" + str(right) + "] - L[" + str(left) + "] = " + str(L[right] - L[left]))
    num = max(num, L[right] - L[left])
    if left == 0 and S[0] == "0":
        left += 1
    else:
        left += 2
    right += 2
if S[-1] == "0":
    right -= 1
    # print("L[" + str(right) + "] - L[" + str(left) + "] = " + str(L[right] - L[left]))
    num = max(num, L[right] - L[left])
print(num)
