N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
if A < B:
    B = A
if B < C:
    C = B
if C < D:
    D = C
if D < E:
    E = D
print(5 + (N - 1) // E)
