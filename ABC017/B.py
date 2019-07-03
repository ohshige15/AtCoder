X = input()
X = X.replace("ch", "").replace("o", "").replace("k", "").replace("u", "")
print("YES" if len(X) == 0 else "NO")
