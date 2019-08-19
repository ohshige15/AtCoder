m = int(input()) / 1000
if m < 0.1:
    print("00")
if 0.1 <= m <= 5:
    print("{0:02d}".format(int(m * 10)))
if 6 <= m <= 30:
    print(int(m) + 50)
if 35 <= m <= 70:
    print(int((m - 30) / 5 + 80))
if 70 < m:
    print(89)
