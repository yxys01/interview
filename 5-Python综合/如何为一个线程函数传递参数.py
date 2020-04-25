import threading
# 线程函数
def func1(s,fun):
    print('正在执行函数func1')
    # 相当于一个函数指针（调用传入的参数函数）
    fun(s)

def ff(s):
    print(f'ff输出了{s}')

# 创建一个类的实例，这个实例指定我们要执行的线程函数func1，传入参数args
t1 = threading.Thread(target=func1,args=('hello world',ff))
t1.start()
