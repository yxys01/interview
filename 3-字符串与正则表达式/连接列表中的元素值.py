'''
q1
'''

a = ['a','b','c','d','e']
s = ""
print(s.join(a))
# 分隔符使用方式
s = "##"
print(s.join(a))

'''
q2
'''
dirs = '','usr','local','nginx',''
print(dirs)
linuxPath = '/'.join(dirs)
print(linuxPath)
windowPath = 'C:' + '\\'.join(dirs)
print(windowPath)

# 注意join函数里面的类型必须为字符串类型
num = [1,2,3,4,5]
print(s.join(str(num)))
