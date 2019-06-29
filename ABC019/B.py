S = input()
result = ""
now = S[0]
num = 1
for s in S[1:]:
    if now == s:
        num += 1
        continue
    result += now + str(num)
    now = s
    num = 1
result += now + str(num)
print(result)
