# 第一题：*和**的作用

# 单行（*）
# 以元组形式导入
# 可变参数
def fun1(param1,*param2):
    print('param1:',param1)
    print('param2:',param2,type(param2))

fun1(1,2,3,4,5)

# 如果可变参数不是最后一个参数，那么为可变参数后面的形参指定参数值，必须用命名参数
def fun2(param1,*param2,x):
    print('param1:',param1)
    print('param2:',param2,type(param2))
    print('x:',x)

fun2(1,2,3,4,5,x = 6)

# 双星（**）
# 以字典形式导入 key 和 value
def fun3(param1,**param2):
    print('param1:',param1)
    print('param2:',param2,type(param2))

fun3(1,a = 2, b = 3, c = 4, d = 5) # 不允许key重复

# 第二题：如何合并列表和字典

# 列表
a = [1,2,3]
b = [4,5,6]

# 1、+
c = a + b
print(c)

# 2、extend (改变a)
a.extend(b)
print(a)

# 3、
a = [1,2,3]
b = [4,5,6]

x = [a,b]
print(x) # [[1, 2, 3], [4, 5, 6]]

x = [*a, *b] # 将a,b 当成一个列表整个导入
print(x)

# 字典
a = {'A':1,'B':2}
b = {'C':3,'D':4}
# c = {'A':1,'B':4,'C':3,'D':4}
c = {**a, **b}
print(c)

