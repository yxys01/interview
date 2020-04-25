class MyClass:
    def __init__(self):
        self.value = 0

    '''
    法1
    def __gt__(self, other): # 大于符号 （升序）
        return self.value > other.value # 若<则是降序
    '''

    '''
    法2
    
    def __lt__(self, other): # 小于符号  （升序）
        return self.value < other.value # 若>则是降序
    '''

my1 = MyClass()
my1.value = 20

my2 = MyClass()
my2.value = 10

my3 = MyClass()
my3.value = 30

a = [my1,my2,my3]
print(a)

# a.sort()
# '<' not supported between instances of 'MyClass' and 'MyClass' MyClass类不支持'<'

# 法3
import operator
#a.sort()

a.sort(key=operator.attrgetter('value'))
b = sorted(a,key=operator.attrgetter('value'))

# 第一题：
print(a[0].value)
print(a[1].value)
print(a[2].value)
print(b[0].value)

# 第二题：降序排列

a.sort(key=operator.attrgetter('value'),reverse=True)

print(a[0].value)
print(a[1].value)
print(a[2].value)
