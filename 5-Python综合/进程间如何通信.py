from multiprocessing import Queue,Process
# 队列，进程

import time,random
# 列表是数据源；在队列中读取数据源，将列表中的值添加到队列，然后从队列中读取该值
list1 = ["java","Python","JavaScript"]

def write(queue):
    for value in list1:
        print(f'正在向队列中添加数据-->{value}')
        # 异步添加
        queue.put_nowait(value)
        time.sleep(random.random())

def read(queue):
    while True:
        # 如果队列不为空，就读
        if not queue.empty():
            # 获取值
            value = queue.get_nowait()
            print(f'从队列中取到的数据为-->{value}')
            time.sleep(random.random())
        else:
            break

# 创建队列实例
queue = Queue()

# 创建两个进程；一个写一个读
write_data = Process(target=write,args=(queue,))
#?这里为什么(queue,);args= 这里参数需要一个元组
read_data = Process(target=read,args=(queue,))

write_data.start()
# 等待写完
write_data.join()

read_data.start()
# 等待
read_data.join()
print('ok')