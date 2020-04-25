a = ['a','b','c','d']
b = [1,2,3,4]
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# zip()返回一个对象。如需展示列表，需手动 list() 转换。
# 如果a,b长度不一，按照最短的进行压缩
print(zip(a,b)) # <zip object at 0x10c7b5b40>
print(list(zip(a,b)))
print(dict(zip(a,b)))

fields = ('id','name','age')
records = [['01','Bill','20'],['02','Mike',30]]
result = []
'''
[
{'id':'01','name':'Bill','age':'20'},
{'id':'02','name':'Mike','age':'30'}
]
'''
for record in records:
    result.append(dict(zip(fields,record)))
print(result)