'''


'''

nestedList =[4,[1,2,[3,5,6]],[4,3,[1,2,[4,5]],2],[1,2,4,5,7]]
print(nestedList)

def enumList(nestedList):
    try:
        for subList in nestedList:
            # 假设subList中都是列表，继续迭代；递归操作
            for element in enumList(subList):
                yield element
    # 如果是单个值，没办法迭代，就会抛出异常
    except TypeError:
        yield nestedList # 迭代单个值

for num in enumList(nestedList):
    print(num, end= ' ')
print()
print(list(enumList(nestedList)))