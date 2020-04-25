'''
nums = [1,2,-2,-1,5,-4]

索引：i,j
i-子序列开始的位置；j-子序列结束的位置
i = 3,j = 5

乘积函数：
mul(i,j) = mul(0,j) / mul(0,i)

mul(0,j)
0:需要重新开始
<0:应该找到前面最大的负数 mul(0,i)该为最大的负数；最大的负数，绝对值才最小，作为除数，才能使mul(i,j)最大
>0:最小的正数 mul(0,i)该为最小的正数，绝对值才最小，作为除数，才能使mul(i,j)最大

'''
# nums-列表
def maxMul(nums):
    # nums为空直接退出
    if not nums:return
    # 目前的累计乘积 mul(0,j)
    cur_mul = 1

    # 前面最小的正数 mul(0,i)
    min_pos = 1

    # 前面最大的负数 mul(0,i)（float("-inf") 负无穷） 除了inf外的其他数除以inf，会得到0
    max_neg = float("-inf")
    # 结果 i-j的乘积 mul(i,j)
    result = float("-inf")

    for num in nums:
        # mul(0,j)
        cur_mul *= num

        if cur_mul > 0:
            # 找到最小的正数
            # 结果mul(i，j)要最大  result 和 mul(0,j) / mul(0,i)取更大的
            result = max(result, cur_mul // min_pos)
            # 结果最大，取最小正数
            min_pos = min(min_pos, cur_mul)
        elif cur_mul < 0:
            # 取最大的负数
            if max_neg != float("-inf"):
                result = max(result, cur_mul // max_neg)
            else:
                # 如果max_neg是负无穷，那它肯定不是最大的，直接和当前num进行比较
                result = max(result, num)
            max_neg = max(max_neg, cur_mul)
        else: # = 0
            # 重新开始
            cur_mul = 1
            min_pos = 1
            max_neg = float("-inf")
            result = max(result,num)
    return result

data = [1, 2, -2, 0, 5, -4]
print(maxMul(data))
data = [1,2,-2,-1,5,-4]
print(maxMul(data))
