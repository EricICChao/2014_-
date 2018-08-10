__author__ = 'Eric'

import re

a = '趙翊清是趙翊清是趙二輕。'
b = ['翊清是趙翊','趙翊清是趙二輕','']
c = 'eric is 趙翊清'
d = ['eric is 趙翊清',' 趙翊清是eric.','Eric is eric,']
e = '趙翊清,是,趙翊清,是趙二輕。'
f = '趙翊清,是趙翊清是趙二輕。'
g = '趙翊清 是趙翊清 是趙二輕。'

h = '趙翊清,是 趙翊清是趙二輕。'
i = '趙翊清 是 趙翊清 是趙二輕。'
j = ',是 趙翊清 是趙二輕。'
k = '趙翊清,是 趙翊清是趙二輕。是趙翊清'
#拆解字串中的單字
test_1 = re.findall(r"\b\w+\b", c)
print(test_1)
test_2 = re.findall(r"\b\w+\b", a)
print(test_2)
#比對字串中的中文單字
test_3 = re.findall(r"\b趙翊清\b", a)   #錯誤比對
print(test_3)
test_4 = re.findall(r"(?u)\b趙翊清\b", c)   #用c字串比對得到
print(test_4)
test_5 = re.findall(r"(?u)\b趙翊清\b", a)   #用字串a比對不到
print(test_5)
#是不是因為a字串全部的字連在一起，沒空格或隔開，所以比對不到?
test_6 = re.findall(r"(?u)\b趙翊清\b", e)   #比對得到，且顯示出關鍵字有比對到的數量
print(test_6)
test_7 = re.findall(r"(?u)\b趙翊清\b", f)   #比對得到，但只顯示單一個 '趙翊清'
print('test_7:')
print(test_7)
test_8 = re.findall(r"(?u)\b趙翊清\b", g)   #比對得到，但只顯示單一個 '趙翊清'
print('test_8:')
print(test_8)
#要找的中文單字或英文單字，除非關鍵字被像 " ,關鍵字," 或是被 " 關鍵字 "用兩個空格或標點符號(逗點等等)隔開，否則永遠只找得到那一個完全隔開的關鍵字而已
#請比較test_7與test_9，test_8與test_10，和上面的test_6
test_9 = re.findall(r"(?u)\b趙翊清\b", h)   #比對得到，但只顯示單一個 '趙翊清'
print('test_9:')
print(test_9)
test_10 = re.findall(r"(?u)\b趙翊清\b", i)   #比對得到，且顯示出關鍵字有比對到的數量
print('test_10:')
print(test_10)


#比對中文時，建議加入下面的count()一起比對較保險，只要不為0，就執行......
test_11 = re.search(r"(?u)\b趙翊清\b", a)   #re.search()時，關鍵字和其他字連成一字串全，找不到
print('test_11:')
print(test_11)
test_12 = re.search(r"(?u)\b趙翊清\b", j)   #re.search()時，比對得到，但是關鍵字必須和其他自隔離開來
print('test_12:')
print(test_12)
print(j.count("趙翊清"))
print(k.count("趙翊清"))

#比對英文時，建議下面兩組加入搜尋
test_13 = re.search(r"(?u)\beric\b", c)
print('test_13:')
print(test_13)
test_14 = re.search(r"\beric\b", c)
print('test_14:')
print(test_14)

"""
比對中文關鍵字時，請使用Unicode模式，加上(?u)，範例如下:
r"(?u)\b中文關鍵字\b"

re.findall找到的東西會放進list裡


上述程式碼的執行結果:
['eric', 'is', '趙翊清']
['趙翊清是趙翊清是趙二輕']
[]
['趙翊清']
[]
['趙翊清', '趙翊清']
test_7:
['趙翊清']
test_8:
['趙翊清']
test_9:
['趙翊清']
test_10:
['趙翊清', '趙翊清']
test_11:
None
test_12:
<_sre.SRE_Match object; span=(3, 6), match='趙翊清'>
1
3
test_13:
<_sre.SRE_Match object; span=(0, 4), match='eric'>
test_14:
<_sre.SRE_Match object; span=(0, 4), match='eric'>
"""
