N = int(input())
A = list(map(int, input().split()))
result = - 10 ** 9
for i in range(N):
    taka_m = - 10 ** 9
    aoki_m = - 10 ** 9
    for j in range(N):
        if i == j:
            continue
        i_ = i
        j_ = j
        if j_ < i_:
            i_, j_ = j_, i_
        taka = sum(A[i_:j_+1:2])
        aoki = sum(A[i_+1:j_+1:2])
        if aoki_m < aoki:
            taka_m = taka
            aoki_m = aoki
    result = max(taka_m, result)
print(result)
