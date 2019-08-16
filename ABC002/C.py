a_x, a_y, b_x, b_y, c_x, c_y = map(int, input().split())
c_x -= a_x
c_y -= a_y
b_x -= a_x
b_y -= a_y
print(abs(b_x * c_y - b_y * c_x) / 2)
