N = int(input())
S = input().split()
if all([i in S for i in ("P", "W", "G", "Y")]):
    print("Four")
else:
    print("Three")
