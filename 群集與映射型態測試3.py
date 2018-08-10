a = {'a': [2,3,4], 'b': [3,4,5]}
b = {'a': [1,3,4,5], 'C': [2,5,11]}

c = FuzzyDisc(a)
print(c)

"""類別呼叫和引用
>>> from fuzzydict import FuzzyDict
>>> fdict = FuzzyDict(0.5) # setting a threshold range from 0.0 to 1.0
>>> # < Assign some values to the 'fdict'>
>>> fdict
>>> {'0123456789': 0, 'X123456789': 1, 'XX23456789': 2, 'XXX3456789': 3, 'XXXX456789': 4, 'XXXXX56789': 5, 'XXXXXX6789': 6, 'XXXXXXX789': 7, 'XXXXXXXX89':8, 'XXXXXXXXX9':9, 'XXXXXXXXXX': 10}
>>> [key for key in fdict.fuzzy_keys('0123456789')]
['0123456789', 'X123456789', 'XX23456789', 'XXX3456789', 'XXXX456789', 'XXXXX56789']
>>> [value for value in fdict.fuzzy_values('0123456789')]
[0, 1, 2, 3, 4, 5]
>>> fdict.fuzzy_add('0123456789', 1) # bulk add
>>> [(k, v) for (k, v) in fdict.fuzzy_items('0123456789')]
[('0123456789', 1), ('X123456789', 2), ('XX23456789', 3), ('XXX3456789', 4), ('XXXX456789', 5), ('XXXXX56789', 6)]
>>> fdict['0123456789'] # You can also access a FuzzyDict as a normal dict
1

"""


class FuzzyDict(dict):
    def __init__(self, threshold):
        self.threshold = float(threshold)
    def _get_fuzzy_elements(self, key):
        if self.has_key(key):
            yield key, self[key]
        chars = int(len(key) * self.threshold)
        keys = [x for x in self.keys() if len(x) == len(key) and x != key]
        for k in keys:
            match = 0
            for i in range(0, len(key), 1):
                if key[i] == k[i]:
                    match += 1
            if chars <= match and self.has_key(k):
                yield k, self[k]
        StopIteration()
    def assign_object(self, obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                self[k] = v
        else:
            raise TypeError()
    def fuzzy_keys(self, key):
        for k, v in self._get_fuzzy_elements(key):
            yield k
        StopIteration()
    def fuzzy_values(self, key):
        for k, v in self._get_fuzzy_elements(key):
            yield v
        StopIteration()
    def fuzzy_items(self, key):
        for k, v in self._get_fuzzy_elements(key):
            yield k, v
        StopIteration()
    def fuzzy_assign(self, key, value):
        for k, v in self._get_fuzzy_elements(key):
            self[k] = value
    def fuzzy_add(self, key, value):
        for k, v in self._get_fuzzy_elements(key):
            self[k] += value
