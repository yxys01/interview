import turtle # 内置库，海龟作图

# 参数：树干的初始长度; 传入对象
def tree(branch_len,t):
    # 长度不能小于5
    if branch_len > 5:
        # 绘制树干
        # forward() 画笔朝前移动；默认从上到下；
        t.forward(branch_len)
        # 叶子
        if(branch_len - 15) <= 5:
            t.pencolor('green')
        else:
            t.pencolor('black')
        # 改变树干的粗细
        new_pensize = branch_len // 5
        if new_pensize > 0:
            t.pensize(new_pensize)

        # 向右侧旋转20度
        t.right(20)

        # 每截树干-15
        # 绘制右侧分支
        tree(branch_len - 15,t)
        new_pensize = branch_len // 5
        if new_pensize > 0:
            t.pensize(new_pensize)
        # 已向右20度了；现在要向左旋转40度
        t.left(40)

        # 绘制左侧的分支
        tree(branch_len -15,t)
        # 摆正画笔
        t.right(20)
        # 叶子
        if (branch_len - 15) <= 5:
            t.pencolor('green')
        else:
            t.pencolor('black')
        # 画笔归位
        t.backward(branch_len)
# 创建一个海归画图对象
t = turtle.Turtle()
# 新弹出一个窗口
win = turtle.Screen()
# 旋转90，从从上到下改为从下到上
t.left(90)
# 画笔颜色
t.pencolor('black')
# 初始粗细
t.pensize(15)
# 长度70
tree(70,t)
# 显示绘制窗口
win.exitonclick()