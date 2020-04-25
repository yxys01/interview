def maxInWindows(num,size):
    # size小于等于0或窗口尺寸大于列表长度
    if size <= 0 or len(num) < size:
        return []
    length = len(num)
    result = []
    # length - size + 1 有多少个滑动窗口
    for i in range(0,length - size + 1):
        # 每个窗口的最大值
        result.append(max(num[i:i+size]))

    return  result
print(maxInWindows([2,3,4,2,6,2,5,1],3))