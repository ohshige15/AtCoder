from collections import Counter
w = input()
if len([s for s, n in Counter(w).items() if n % 2 != 0]) == 0:
    print("Yes")
else:
    print("No")
