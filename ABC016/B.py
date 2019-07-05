A, B, C = map(int, input().split())
if A + B == C and A - B == C:
  print("?")
  exit()
if A + B == C:
  print("+")
  exit()
if A - B == C:
  print("-")
  exit()
print("!")
