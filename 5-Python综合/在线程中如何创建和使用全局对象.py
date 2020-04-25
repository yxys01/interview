'''
threading.local 类
通过实例化该类，将其变成一个对象，然后该对象可以保存全局变量
但是这个全局变量只针对当前的线程，即不能在多线程之间共享

'''
import threading
import time
a = threading.local()

# 线程函数
def worker():
    a.x = 0
    # 多线程是否能互相影响
    for i in range(20):
        time.sleep(0.01)
        a.x += 1
    print(threading.current_thread(),a.x)

# 启用十个线程函数
for i in range(10):
    threading.Thread(target=worker).start()

# 每个线程后面都是20，说明a只是针对每个线程的，多个线程之间不能共享a