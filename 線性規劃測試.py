a = [1,2,3,4,5,6]
b = [1,2,3,4]
c = {(1,2,3),(4,5,6),(1,3,9)}
arr = []
arr_2 = []


for (x,y,z) in c:
    func = x*2+pow(y,2)+z
    arr_2.append(func)
    if max(arr_2):
        print(x,y,z)
print(max(arr_2))



print(c.sort())


print("======================================")
"""left_x = []
right_x = []
left_attr = []
right_attr = []
for x in u_set:
    func = x*2+y**2+z
        if x <= m and 0 <= func_a < 1:
            left_attr.append(func_a)
            left_x.append(x)
        if x >= m and 0 <= func_b < 1:
            right_attr.append(func_b)
            right_x.append(x)
    left_xx = dict(zip((left_x),(left_attr)))
    right_xx = dict(zip((right_x),(right_attr)))
    return left_xx, right_xx, m


"""
