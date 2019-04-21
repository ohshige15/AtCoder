s = input()
i = s.index("A")
j = len(s) - s[::-1].index("Z") - 1
print(j - i + 1)
