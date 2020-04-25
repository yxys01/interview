a = [4,3,6,5]

print(a)

del a[2]
# del(a[2]) 两种方式都一样，但是del不是函数，是关键字
print(a)

# pop是列表的一个方法
print(a.pop(1))
print(a)

print(a.pop()) # 不加参数，删除最后一个元素
print(a)

# del 根据索引删除列表元素，但没有返回值
# pop 根据索引弹出列表元素，并返回该元素，同时从列表中删除该元素