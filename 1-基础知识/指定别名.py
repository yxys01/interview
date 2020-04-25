# 指定别名 as
import math as m
print(m.sin(20))
# 使用别名后再使用原模块名前缀会报错
#print(math.sin(1.23))

from math import cos as c
print(c(3))

#print(cos(12))