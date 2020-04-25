import re
'''
1.表示浮点数的正则表达式 -？有可能存在问号  \d+ 任意多的数字  （\.\d+)? 有可能有.数字 也可能没有 
2.格式化浮点数  format
3.如何替换原来的浮点数 sub（只返回替换结果） subn （返回元组，不仅有替换结果还有替换次数）
'''

result = re.subn('-?\d+(\.\d+)','##','PI is 3.141592654,e is 2.71828183. -0.2 + 1.3 =1.1')
print(result) # 将所有浮点数替换成##
print(result[0])
print(result[1])

def fun(matched):
    return format(float(matched.group()),'0.2f')

result = re.subn('-?\d+(\.\d+)',fun,'PI is 3.141592654,e is 2.71828183. -0.2 + 1.3 =1.1')
print(result)