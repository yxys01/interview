# 线程池
from concurrent.futures import  ThreadPoolExecutor

# 进程池
from concurrent.futures import ProcessPoolExecutor
import time,os,threading

def work(n):
    print(f'给{n}打电话，进程号：{os.getpid()}，线程号{threading.current_thread()}')
    time.sleep(3)
    print(f'{n}通话结束，进程号：{os.getpid()}，线程号{threading.current_thread()}')
    print('\n')

userlist = ['刘德华','吴彦祖','梁朝伟','周杰伦','林俊杰']

# # 1、创建线程池  推荐多使用多线程或线程池
# pool = ThreadPoolExecutor(max_workers=3)
#
# # # 循环指派任务
# # for user in userlist:
# #     # 2、指定对应任务和参数
# #     pool.submit(work,user)
#
# # 2、指定对应任务和参数
# [pool.submit(work,user) for user in userlist]
#
# # 3、关闭线程池
# pool.shutdown()


if __name__ == '___main__':
    # 1、创建进程池
    pool = ProcessPoolExecutor(max_workers=3)

    # 2、指定对应任务和参数
    [pool.submit(work, user) for user in userlist]

    # 3、关闭进程池
    pool.shutdown()