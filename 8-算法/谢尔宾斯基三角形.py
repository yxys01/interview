import turtle

# 绘制单个三角形
# [[x1,y1],[x2,y2],[x3,y3]]
def draw_triangle(points, color, t):
    # 填充颜色
    t.fillcolor(color)
    # 抬起画笔；否则绘制轨迹
    t.up()
    # 将画笔移动到第一个点
    t.goto(points[0][0], points[0][1]) # (x1,y1)
    # 画笔落下
    t.down()
    # 开始填充
    t.begin_fill()
    # 画笔在三个点之间移动
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    # 画笔移回来变成封闭三角形
    t.goto(points[0][0], points[0][1])
    t.end_fill()

# 计算两点的中位点的坐标
def mid_point(p1,p2):
    return ((p1[0] + p2[0])/2,(p1[1] + p2[1])/2)

# 绘制谢尔宾斯基三角形
def  sierpinski(points,degree,t):
    # 定义颜色
    colormap = ['blue','red','green','yellow','violet','orange']
    # 绘制大的三角形
    draw_triangle(points,colormap[degree - 1],t)
    # 设置终止条件
    if degree >= 0:
        # 绘制左下角三角形
        sierpinski([points[0], mid_point(points[0], points[1]), mid_point(points[0], points[2])], degree - 1, t)
        # 绘制上方的三角形
        sierpinski([points[1], mid_point(points[0], points[1]), mid_point(points[1], points[2])], degree - 1, t)
        # 绘制右下角三角形
        sierpinski([points[2], mid_point(points[2], points[1]), mid_point(points[0], points[2])], degree - 1, t)

t = turtle.Turtle()
win = turtle.Screen()
points = [[-200,-100],[0,200],[200,-100]]
sierpinski(points,4,t)
win.exitonclick()