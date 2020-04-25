def numberOfOneBetween(n):
    count = 0
    for i in range(1,n+1):
        for i in str(i): # 将整数变为字符串遍历
            if i == '1':
                count += 1
    return count
print(numberOfOneBetween(200))