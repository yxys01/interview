import time,os,threading
from multiprocessing import Process # 进程
from threading import  Thread # 线程


def work(n):
    print(f'给{n}打销售电话，进程号：{os.getpid()}，线程号{threading.current_thread()}')
    time.sleep(3)
    print(f'销售电话结束:{n}，进程号：{os.getpid()}，线程号{threading.current_thread()}')

userlist = ['刘德华','张学友','梁朝伟']
# 普通方式来完成
# 启动了一个进程，进程中有一个主线程
# for item in userlist:
#     work(item)



# 阻塞终止进程的执行
# for i in plist:
#     i.join()

# 进程池相关代码要放在主函数中
# if __name__ == '__main__':
#     # 多进程 类似于 创建多个部门来完成这项工作;多进程线程号一样
#     plist = []
#     for item in userlist:
#         # 循环创建进程
#         p = Process(target=work, args=(item,))
#         # 生成进程
#         p.start()
#         # 把创建的进程加入到列表中
#         plist.append(p)
#     阻塞终止进程的执行
#     [i.join() for i in plist]

# 多线程 类似与 给这个部门增加人手来参加工作；多线程进程号相同
plist = []
for item in userlist:
    # 循环创建线程
    p = Thread(target=work, args=(item,))
    # 生成线程
    p.start()
    # 把创建的线程加入到列表中
    plist.append(p)
# 阻塞终止线程的执行
[i.join() for i in plist]