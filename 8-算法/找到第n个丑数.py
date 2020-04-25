'''
只包含2、3、5中的1个或多个因子的数称为丑数

6
14：不是丑数

下一个丑数必定是数组中的某一个丑数A*2、B*3、C*5中最小的值

M2，之前的丑数*2都小于当前最大的丑数
    之后的丑数*2都大于当前最大的丑数

M3，之前的丑数*3都小于当前最大的丑数
    之后的丑数*3都大于当前最大的丑数

M5，之前的丑数*5都小于当前最大的丑数
    之后的丑数*5都大于当前最大的丑数
'''

def getUglyNumber(index):
    if index < 1:
        return 0
    # 丑数放在数组里，第一个数是1
    res = [1]
    # 索引默认为0
    t2 = t3 = t5 = 0
    # 下一个丑数值的索引
    nextdex = 1
    # 找下一个丑数
    while nextdex < index:
        # 最小的丑数
        minNum = min(res[t2]*2, res[t3] * 3, res[t5]*5)
        res.append(minNum)
        # 找下一个t2、t3、t5的索引；
        # 直到找到大于minNum的数的索引
        while res[t2] * 2 <= minNum:
            t2 += 1
        while res[t3] * 3 <= minNum:
            t3 += 1
        while res[t5] * 5 <= minNum:
            t5 += 1
        nextdex += 1
    return res[nextdex - 1] # 得到第n个（从0 开始所以减1）
print(getUglyNumber(10))
print(getUglyNumber(100))