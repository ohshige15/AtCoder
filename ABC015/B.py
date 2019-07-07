N = int(input())
A = [a for a in map(int, input().split()) if a != 0]
print(int((sum(A) + len(A) - 1) // len(A)))
