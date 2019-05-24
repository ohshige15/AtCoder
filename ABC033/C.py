S = input()
num = 0
for s in S.split("+"):
    if any([n == "0" for n in s.split("*")]):
        continue
    num += 1
print(num)
