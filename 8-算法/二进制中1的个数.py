# 把某一位变成1，其他位都是0
# 如果是0，计数器不加1；如果是1，计数器加1

def oneNumber(n):
    print(bin(n))
    if n < 0:
        n = n & 0xffffffff # 补码
    print(bin(n))
    m = len(bin(n)) - 2
    count = 0
    '''
    1101 =13
    
    1000 = 8 count++
    0100 = 4 count++
    0000 = 0 count 不变
    0001 = 1 count++
    '''
    for i in range(0,m):
        # n与2的i次方 按位于；将特定位变为1，其他位都是0
        if n & 2 **i != 0:
            count += 1
    return count

print(oneNumber(13))
print(oneNumber(-1))