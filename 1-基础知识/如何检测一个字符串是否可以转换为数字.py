# 第一题：检测字符串是否为数字
s1 = '12345'
print('12345是数字：',s1.isdigit())
print(int(s1))

s2 = '12345a'
print('12345a是数字：',s2.isdigit())
print('12345a是字母数字混合形式：',s2.isalnum())

# 下划线既不属于数字也不属于字母
s3 = '12_345a'
print('12_345a是字母数字混合形式：',s3.isalnum())

# 判断是不是空格
print("    ".isspace())

# 检测字符串中是否为整数
print("12.45".isdecimal())

# 检测字符串中是否为字母
print("asdc3".isalpha())

# 第二题：如果将字符串转换为整数，如何做才安全
s1 = "1234"
print(int(s1))

s2 = '1234a'
# print(int(s2))# 抛出异常

# 第一种：判断
if s2.isdigit():
    print(int(s2))
else:
    print('s2不是数字，无法转换')

# 第二种
try:
    print(int('223aa'))
except Exception as e:
    print('223aa不是数字，无法转换')
    print(e)