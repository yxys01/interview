'''
对资源的访问次数进行控制，就要使用信号量

信号量：最古老的同步原语之一，是一个计数器。

当资源释放时，计数器就会递增，当申请资源时，计数器就会递减
'''
from threading import BoundedSemaphore
MAX = 3
# 信号量最大拥有的资源是3；最多可以申请3次资源
semaphore = BoundedSemaphore(MAX)
# 剩余资源 3
print(semaphore._value)
# 申请资源
semaphore.acquire()
# 剩余资源 2
print(semaphore._value)
# 申请资源
semaphore.acquire()
# 剩余资源 1
print(semaphore._value)
# 申请资源
print(semaphore.acquire()) # 参数默认为True，申请成功返回True
# 剩余资源 0
print(semaphore._value)

# 剩余资源(_value)为0时，再次调用acquire()申请资源，会被阻塞
# semaphore.acquire() # 阻塞时，进程一直处于进行时

# 如果没有资源可以申请时，再次调用acquire()方法，返回False，而不会阻塞
print(semaphore.acquire(False))
# 剩余资源 0
print(semaphore._value)
# 第一次释放资源（要释放MAX次才行）
semaphore.release()
print(semaphore._value)

# 第二次释放资源
semaphore.release()
print(semaphore._value)

# 第三次释放资源
semaphore.release()
print(semaphore._value)

# 第四次释放资源；现在已经没有资源被占用，所以会抛出异常：Semaphore released too many times
# semaphore.release()
# print(semaphore._value)