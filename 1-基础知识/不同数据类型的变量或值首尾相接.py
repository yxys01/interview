# 字符串与字符串之间连接的方式有5种
#### 第一种：+（加号 ）
s1 = 'hello'
s2 = 'world'
s = s1 + s2
print(s)

#### 2:直接连接
s = "hello""world"
print(s)

#### 3:用逗号（,）连接(只能输出控制台)
#### 希望变成变量：标准输出重定向
from io import StringIO
import sys
old_stdout = sys.stdout # 先保存标准输出，然后再恢复
result = StringIO() # 标准输出放到字符串中
sys.stdout = result
print('hello','world') # 处理完之后，这里没有输出，输出值在result之中
sys.stdout = old_stdout # 恢复标准输出
result_str = result.getvalue() # 得到最终结果
print("用逗号连接：",result_str)

#### 4:格式化（好处：给要格式化的字符串添油加醋，可以添加其他东西(添加一对'<>')）
s = '<%s><%s>' % (s1,s2)
print('格式化：',s)

#### 5：join
s = " ".join([s1,s2]) # 连接一个列表里面的值
print("join连接:",s)

### 第2题：字符串与非字符串直接如何连接
# 1：加号
n = 20
s = s1 + str(n)
print(s)
v = 12.44
b = True
print(s1 + str(n) + str(v) + str(b))

# 2:格式化（可以格式化非字符串类型）
s = '<%s> <%d> <%.2f>' %(s1, n, v)
print('格式化：', s)

# 3:重定向
from io import StringIO
import sys
old_stdout = sys.stdout # 先保存标准输出，然后再恢复
result = StringIO() # 标准输出放到字符串中
sys.stdout = result
print(s1,True,n,v,sep='*') # 处理完之后，这里没有输出，输出值在result之中
sys.stdout = old_stdout # 恢复标准输出
result_str = result.getvalue() # 得到最终结果
print("用*连接：",result_str)

### 第3题：
class MyClass:
    def __str__(self):
        return 'This is a MyClass Instance.'
    pass
my = MyClass()
s = s1 +str(my)
print(s) # hello<__main__.MyClass object at 0x105c282d0>

