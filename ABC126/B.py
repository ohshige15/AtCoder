S = input()
a = S[:2]
b = S[2:]
if "01" <= a <= "12":
    if "01" <= b <= "12":
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if "01" <= b <= "12":
        print("YYMM")
    else:
        print("NA")
