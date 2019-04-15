from itertools import zip_longest
O = input()
E = input()
print("".join([(o or "") + (e or "") for o, e in zip_longest(O, E)]))
