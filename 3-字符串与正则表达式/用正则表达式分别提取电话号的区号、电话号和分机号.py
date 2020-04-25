# q1
import re

m = re.search('(\d{3})-(\d{7,})-(\d{3,})','我的公司座机是024-123456788-5432') #{7,}至少7位
if m is not None:
    print(m.group())
    print(m.groups()) # 要获取分组，先要用（）分组
    print(m.groups()[0])
    print(m.groups()[1])
    print(m.groups()[2])
