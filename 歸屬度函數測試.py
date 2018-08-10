d = {5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

m =12.5
a_left = 6
b_right = 20
left_x = []
right_x = []
left_attr = []
right_attr = []
#left_xx = []
#right_xx = []
for x in d:
    func_a = (m-x) / a_left
    func_b = (x-m) / b_right
    if x < m and 0 <= func_a < 1:
        left_attr.append(func_a)
        left_x.append(x)
    if x > m and 0 <= func_b < 1:
        right_attr.append(func_b)
        right_x.append(x)
left_xx = dict(zip((left_x),(left_attr)))
right_xx = dict(zip((right_x),(right_attr)))

print(left_xx)
print(right_xx)
