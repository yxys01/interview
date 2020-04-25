'''
copy：只复制深层对象的引用(复制的深层对象和原始的深层对象所指的是一个对象)
deepcopy:复制深层对象本身

'''

import copy
a = [1,2,3,4,['a','b']] # ['a','b']相当于列表的第二层（深层对象）

c = copy.copy(a) # 浅拷贝;复制最初的值

d = copy.deepcopy(a) # 深拷贝

print(c) # c中的['a','b']和a中的['a','b']是一个对象
print(d)
print('----------')
a.append(5)
print(a)
print(c)
print(d)
print('----------')

a[4][0] = 'x'
print(a)
print(c) # 因为c是浅拷贝，a的['a','b']和c的是一个对象，所以a变c也变
print(d)