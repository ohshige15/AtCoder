s = input()
k = int(input())
result = set()
for i in range(len(s) - k + 1):
    result.add(s[i:i + k])
print(len(result))
