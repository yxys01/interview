'''
q1

with语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的"清理"工作
主要用于释放资源
比如说：文件适用后的自动关闭；线程中锁的自动获取和释放
'''
f = open('files/readme.txt','r')
data = f.read()
print(data)
f.close()
'''
这么写存在两个问题：
1、没有关闭文件
2、即使关闭了文件，但在关闭之前如果抛出异常，仍然会无法关闭文件
'''
f = open('files/readme.txt','r')
try:
    data = f.read()
except:
    print('抛出异常')
# 防止了第二个问题；仍然存在第一个问题；即没有调用close()，就无法关闭文件
finally:
    f.close()

# 保证肯定能关闭文件
# with语句执行完，自动调用close()方法
with open('files/readme.txt','r') as f:
    data = f.read()
    print(data)

'''
q2:将with语句用于自定义的类

魔法函数
__enter__(函数调用之前调用)

__exit__（类里函数调用之后调用）

'''
class MyClass:
    def __enter__(self):
        print('__enter__ is call!')
        return self

    def process1(self):
        print('process1')

    def process2(self):
        # 抛出异常
        x = 1/0
        print('process2')
    # exc_type:传入   traceback:抛出异常时使用；无异常返回空
    def __exit__(self, exc_type, exc_val, traceback):
        print('__exit__ is call')
        print(f'type:{exc_type}')
        print(f'value:{exc_val}')
        print(f'trace:{traceback}')

with MyClass() as my:
    my.process1()
    my.process2()

