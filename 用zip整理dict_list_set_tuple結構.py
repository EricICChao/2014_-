Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=dict{zip((1,2,3,4),("aa", "bbb", 'c', "ddfe"))}
SyntaxError: invalid syntax
>>> x=dict(zip((1,2,3,4),("aa", "bbb", 'c', "ddfe")))
>>> x
{1: 'aa', 2: 'bbb', 3: 'c', 4: 'ddfe'}
>>> x=dict(zip((1,2,3,4),("aa", "bbb", 'c', "ddfe",'d')))
>>> x
{1: 'aa', 2: 'bbb', 3: 'c', 4: 'ddfe'}
>>> x=dict(zip((1,2,3,4),(["aa", "bbb"], 'c', "ddfe",'d')))
>>> x
{1: ['aa', 'bbb'], 2: 'c', 3: 'ddfe', 4: 'd'}
>>> x=dict(zip((1,2,3,4),(["aa", "bbb"], 'c', "ddfe")))
>>> x
{1: ['aa', 'bbb'], 2: 'c', 3: 'ddfe'}
>>> 
