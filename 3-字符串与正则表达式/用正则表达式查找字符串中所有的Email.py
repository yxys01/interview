import re

s = '我的Email地址是abcd@163.com,你的Email是多少呢？是xyz@122.net吗？或者是ccc@125.org'

# 查找所有的，符合条件的字符串
prefix = '[0-9a-zA-Z]+@[0-9a-zA-Z]+\.'
result = re.findall(prefix + 'com|' + prefix + 'net',s,re.I) # re.I 忽略大小写 | 或者
print(result)