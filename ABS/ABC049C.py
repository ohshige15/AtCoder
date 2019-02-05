s = input()
suffix_list = ["dream", "dreamer", "erase", "eraser"]
while s != "":
    for suffix in suffix_list:
        x = s.rfind(suffix)
        if s.endswith(suffix) and x != -1:
            s = s[0:x]
            break
    else:
        print("NO")
        exit()
print("YES")
