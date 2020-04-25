# 导入Python模块的方式
import math
#from后面跟着和import后面跟着的模块一样
#from后面的import跟着的是模块里的成员名，类名，函数名(可跟多个)
#这样的优势在于，导入函数名之后可以不需要再跟模块名
from math import cos,tan
#*可以提前所有方法，且不需要前缀
from math import *
print(math.sin(1.23))
print(cos(2.34))
print(tanh(1.23))

