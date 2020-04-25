# m报数
def lastRemaining(n, m):
    if n < 1 or m < 1:
        return -1
    # 初始值
    temp = 0
    # 对n进行迭代
    for i in range(1,n+1):
        # 套公式
        temp = (temp + m) % i
    return temp
print(lastRemaining(10,12))
print(lastRemaining(10,123))
