# q1
import re
# 用来判断匹配；如果不匹配返回None
print(re.match('.*hello','ahello'))

# q2

s = 'Today is 2013-12-12.'
m = re.match('.*\d{4}-\d{2}-\d{2}.*',s)  # \d 表示数字 {4}表示4位 .* 前|后缀
print(m)
if m is not None:
    print(m.group()) # 输出具体匹配的值
