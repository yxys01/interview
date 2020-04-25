# 1.通过索引获取字符串中的某个字符
s1 = 'hello world'
print(s1[0])
print(s1[2])

# 2、分片
print(s1[6:9]) # 取6-8
print(s1[6:])  # 取6到最后
print(s1[::2]) # 隔一个取一个
print(s1[::-1])# 取反

# 3、乘法
s2 = 'xyz'
print(10 * s2)
print(s2 * 8)

# 4、判断字符是否在字符串中
print('b' in s2)
print('y' in s2)
# 判断字符不在字符串中
print('b' not in s2)

# 5、字符串长度
print(len(s1))

# 6、最大最小字符
print(min(s2))
print(max(s2))

#一个字符串相当于用字符组成的元组（不可通过索引改变值）