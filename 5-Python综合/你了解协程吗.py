'''
q1
协程：又称为微线程、纤程，英文名：Coroutine

通过async/awiat语法进行声明，是编写异步应用的推荐方式

举例：
import asyncio

# 主函数
async def main():
    print('hello')
    # 等待1s
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())

q2:协程中有哪两个运行任务的函数，如何使用
1.run
2.create_task
'''
import asyncio
import time

# 异步函数
async def say_after(delay,what):
    # 停留时间
    await asyncio.sleep(delay)
    print(what)


async def myfun():
    print(f'开始时间：{time.strftime("%X")}')
    # 如果用async修饰，必须调用await修饰
    # 如果不加await会抛出异常
    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f'执行完成：{time.strftime("%X")}')

asyncio.run(myfun())

'''
create_task:用来并发运行作为异步任务的多协程
'''
# 注意这里是并发执行，只用了2s，前面那种用了3s
async def myfun1():
    # 建立两个任务
    task1 = asyncio.create_task(
        say_after(1,'hello')
    )
    task2 = asyncio.create_task(
        say_after(2,'world')
    )
    print(f'开始时间：{time.strftime("%X")}')

    # 开始任务
    await task1
    await task2

    print(f'结束时间：{time.strftime("%X")}')

asyncio.run(myfun1())