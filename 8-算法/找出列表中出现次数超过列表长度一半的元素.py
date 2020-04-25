def moreThanHalfNum(numbers):
    d = {}
    maxNum = 'no'
    listCount = len(numbers)

    for n in numbers:
        # 判断字典d是否包含数字n
        if d.get(n) is None:
            # 第一次出现
            d[n] = 1
            # 说明是第一次扫描
            if maxNum == 'no':
                maxNum = n
        # 如果n出现过
        else:
            d[n] += 1
        # d.get(n) > d.get(maxNum) n的出现次数是否大于maxNum
        # 判断n是不是maxNum本身
        if n!= maxNum and d.get(n) > d.get(maxNum):
            # maxNum是最大数
            maxNum = n

        if d.get(maxNum) > listCount // 2:
            return maxNum
    return 'no'

print(moreThanHalfNum([1,1,4,2,2,1,1,1,1,1,1,1]))
print(moreThanHalfNum([1,1,4,2,2,0,0,0,3,3,4,2,4,5,3,1,1,1,1,1,1,1]))