import math


"""set_list = [1,2,3,4,5,6,7,8]

for x in set_list:
    func_ans = 0*pow(1,5)+0*pow(1,4)+0*pow(1,3)+0*pow(1,2)+1*pow(x,1)+0.04
    print(int(func_ans))

for x in set_list:
    func_ans = 0*pow(1,5)+0*pow(1,4)+0*pow(1,3)+0*pow(1,2)+1*pow(x,1)+0.04
    print(func_ans)
for x in set_list:
    func_ans = 0*pow(1,5)+0*pow(1,4)+0*pow(1,3)+0*pow(1,2)+1*pow(x,1)+0.04
    print(float(int(func_ans)))


print("===================================================================")
func_ans = 0*pow(1,5)+0*pow(1,4)+0*pow(1,3)+0*pow(1,2)+1*pow(x,1)+0.04
attr = 23

fuzzyattr_set = [func_ans for x in set_list if func_ans != attr]
fuzzyU_set = [x for x in set_list if func_ans != attr]
  
print(fuzzyU_set)
print(fuzzyattr_set)

print("===================================================================")
clear_set = []

for x in set_list:
    func_ans = 0*pow(1,5)+0*pow(1,4)+0*pow(1,3)+0*pow(1,2)+1*pow(x,1)+0.04
    clear_set.append(func_ans)
    print(clear_set)
print("===================================================================")
clear_set2 = []
for x in set_list:
    func_ans = 0*pow(1,5)+0*pow(1,4)+0*pow(1,3)+0*pow(1,2)+1*pow(x,1)+0.04
    clear_set2.append(func_ans)
print(clear_set2)
"""

print("模糊交集的測試")
from collections import defaultdict



a = {1:20, 2:40, 3:60, 4:80}
b = {1:10, 3:30, 4:50}
c = [1,2,3,4,5,6,7,8,9,10]


print("==============兩組比較===================")
d = defaultdict(set)
d[1].add(1)
d[2].add(2)
d[3].add(3)
d[4].add(4)
d[5].add(5)


e = defaultdict(set)
d[1].add(1)
d[2].add(1)
d[3].add(1)
d[4].add(2)
d[5].add(7)
d[6].add(6)

"""
f
 = defaultdict(set)
f[1].add(1)
f[2].add(1)
f[3].add(1)
f[4].add(2)
f[5].add(7)
f[6].add(6)
"""
print(d)
#print(f)

print("==============兩組比較===================")




g = {1:1,2:2,3:3,4:4,5:5,6:6.1}
h = {1:1.1,2:2.2,3:3.1,4:4.1,5:5.2,6:6.1}
i = g.items()
j = h.items()
k = a.keys()
l = b.keys()


m = k | l
n = i | j   # n以變成一個set了
min_value = min(g, key = lambda k: g[k])
o = i & j


print(i)
print(j)
print(m)
print(n)
print(min_value)
print(o)

#參考檔案: 字典的交集與聯集
#參考檔案: 群集資料相關-字典的len()函式
#字典的len()函式
#len(d)
#Return the number of items in the dictionary d.



print("=======================================================")
abu_set = []
abu_v_set = []
value_set = []
a_set = {1,2,3,4,9,10}
b_set = {2,3,4,5,9,10}
#a和b的元素set屬於u裡面的元素
"""
abu_set = []
value_set = []
for x in a_set & b_set:
    abu_set.append(x)


    
for x in abu_set:     #a_ans是a_set的歸屬度函數，b_ans是b_set的歸屬度函數，
    a_ans = 0.15*pow(x,1)+0.05
    b_ans = 0.17*pow(x,1)+0.01
    if a_ans < b_ans and 0 <= a_ans <= 1:
        value_set.append(a_ans)
    elif b_ans < a_ans and 0 <= b_ans <= 1:
        value_set.append(b_ans)




for x in abu_set:
    if a_ans > 1 or a_ans < 0 or b_ans > 1 or b_ans < 0:
        abu_set.remove(x)

print(value_set)
print(abu_set)
xx = dict(zip((abu_set),(value_set)))
print(xx)
"""
print("=======================================================")
for x in a_set & b_set:
    a_ans = 0.15*pow(x,1)+0.05
    b_ans = 0.17*pow(x,1)+0.01
    if a_ans < b_ans and 0 <= a_ans <= 1:
        value_set.append(a_ans)
        abu_set.append(x)
    elif b_ans < a_ans and 0 <= b_ans <= 1:
        value_set.append(b_ans)
        abu_set.append(x)

print(value_set)
print(abu_set)
xx = dict(zip((abu_set),(value_set)))
print(xx)

print("=========================abs==============================")
for x in a_set:
    a_ans = 0.15*pow(x,1)+0.05
    abu_set.append(x)

gg = sum(abu_set) 
math.fabs(gg)  #math.fabs()是float專用  #math.abs()是int專用  
print(gg)
    





    
