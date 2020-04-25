# 列表和字典

d = {}
d['name'] = 'Bill'
d[10] = 20
d[True] = False
d[12.3] = 20.1

d[(1,2,3)] = [4,5,6]

class Person:
    pass

p1 = Person() # 用对象的地址来作为
p2 = Person()

d[p1] = 'p1'
d[p2] = 'p2'

print(d)
print(d[12.3])

# d[[1,2,3]] = 3 # unhashable type: 'list' 列表作为键值报错，无法使用哈希值
# d[{'a':3}] = 4 # unhashable type: 'dict'
# d[{'a',3,4}] = 5 # unhashable type: 'set'
# 因为key是不能变的。但列表、集合和字典的值是可以变化的，一旦变化，就再也找不到value了