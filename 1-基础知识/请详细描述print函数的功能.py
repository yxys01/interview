# 第一题：用逗号分隔输出的字符串
print("aa","bb",sep=",") # sep后可以接任何内容作为分隔;默认为空格

# 第二题：如何让print不换行
print('hello',end=" ") # end后可以接任何内容作为结尾;默认为回车
print('world')

# 第三题：格式化
s = 'road'
x = len(s)
print('The length of %s is %d' % (s, x))

from io import StringIO
import sys
old_stdout = sys.stdout
result = StringIO()
sys.stdout = result
print('The length of %s is %d' % (s, x))
sys.stdout = old_stdout
result_str = result.getvalue()
print('result_str',result_str,sep=":")
