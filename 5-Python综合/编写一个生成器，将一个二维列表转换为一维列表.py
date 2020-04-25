'''
Python生成器(主要作用是迭代)
本身是一个函数，和普通函数不同，普通函数需要通过return来返回值，而生成器需要用yield来迭代这个值

循环中一个一个获得迭代的值
'''
def myGenerator():
    numList = [1,2,3,4,5,6,7,8]
    for num in numList:
        # return的话只能返回第一个值
        yield num

# 将myGenrator生成器作为for循环中in后面的那个进行迭代
# 将生成器当成一个集合；每迭代一次，yield num就执行一次，执行完了就进行下一次的迭代
for num in myGenerator():
    print(num, end=' ')
print()

'''
[[1,2,3],[4,3,2],[1,2,4,5,7]]

[1,2,3,4,3,2,1,2,4,5,7]
'''
nestedList = [[1,2,3],[4,3,2],[1,2,4,5,7]]

def enumList(nestedList):
    for subList in nestedList:
        for element in subList:
            yield element

for num in enumList(nestedList):
    print(num, end=' ')

numList = list(enumList(nestedList))
print(type(numList))
print(numList)