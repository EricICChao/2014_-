Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = {1,2,2,3,4,5,6,3,2,1,0}
>>> b = {1,2,1,2,1,2,0}
>>> s - b
{3, 4, 5, 6}
>>> c = {"ewqe", 'a'}
>>> s | c
{0, 1, 2, 3, 4, 5, 6, 'ewqe', 'a'}
>>> a = 2^10
>>> a
8
>>> 2^3
1
>>> a = math.pow(2,3)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a = math.pow(2,3)
NameError: name 'math' is not defined
>>> import math
>>> a = math(2,4)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a = math(2,4)
TypeError: 'module' object is not callable
>>> a = pow(2,3)
>>> a
8
>>> b = pow(2,10)
>>> b
1024
>>> s = {"a":[16,21,4], "b":[32,76,81]}
>>> a = {"c":[21,17], "f":[32,98], "g":3, "word":"eric"}
>>> s | a
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s | a
TypeError: unsupported operand type(s) for |: 'dict' and 'dict'
>>> gg = s | a
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    gg = s | a
TypeError: unsupported operand type(s) for |: 'dict' and 'dict'
>>> s.items()
dict_items([('b', [32, 76, 81]), ('a', [16, 21, 4])])
>>> gg = s.items()
>>> kk = a.items()
>>> gg | kk
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    gg | kk
TypeError: unhashable type: 'list'
>>> gg = s.k
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    gg = s.k
AttributeError: 'dict' object has no attribute 'k'
>>> gg = s.keys()
>>> kk = a.keys()
>>> gg | kk
{'g', 'c', 'b', 'a', 'f', 'word'}
>>> 
