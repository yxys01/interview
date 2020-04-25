'''
二叉搜索树：
又称：二叉排序树；二叉查找树
二叉：每个节点最多不超过两个分支（0、1、2个）

当前节点的左子节点不为空的话，左子节点下面的所有的节点都必须小于根节点
当前节点的右子节点不为空的话，右子节点下面的所有的节点都必须大于根节点

访问根节点的次序
前序遍历：先访问根节点，再左节点，最后右节点
中序遍历：先访问左节点，再根节点，最后右节点
后序遍历：先访问左节点，再右节点，最后根节点

根节点

后序：1、 4、7、6、 3、 13、14、10、 8
前序：8,3,1,6,4,7,10,14,13
算法：
1.找到根节点（后序遍历，根节点是最后一个）
2.遍历序列，找到第一个大约等于根节点的元素i，则i左侧为左子树，右侧为右子树
3.判断i右侧的节点是否都比根节点的值大，如果有比根节点的值小，直接返回False；
4.否则用递归的方式继续处理i左侧和右侧的节点；直到递归结束返回True，或者半途返回False
'''
# 传入一个序列
def verifyBST(sequence):
    if not sequence:
        return False
    # 根节点(最后一个元素)
    root = sequence[-1]

    i = 0
    # 倒着迭代
    for node in sequence[i:-1]:
        # sequence[0:-1];除去最后一个根节点的所有值[1, 4, 7, 6, 3, 13, 14, 10]
        # 从前向后扫描，找到第一个大于root的值i
        if node > root:
            break
        i += 1
        # 扫描到i = 5时，break

    # 继续扫描,此时i = 5
    for node in sequence[i:-1]:# sequence[5:-1] [13, 14, 10]
        # 如果找到小于root的值，返回False
        if node < root:
            return False
    # 第四步、递归
    # 如果前面一切正常，left为True
    left = True
    # i=5
    if i > 0:
        # 验证左子树[1, 4, 7, 6, 3]是否为二叉搜索树
        left = verifyBST((sequence[:i])) #sequence[:5] [1, 4, 7, 6, 3]
    right = True
    # i=5;len(sequence)=9-2=7
    if i < len(sequence) - 2 and left: # 这里为什么是len -2？？？len-1吧？
        # 如果左侧为假直接返回False
        right = verifyBST(sequence[i + 1:])
        # right = verifyBST(sequence[i:-1]) ？？？这里应该是[i:-1]吧？

    return left and right

print(verifyBST([1, 4,7,6, 3, 13,14,10, 8 ]))
a = [1, 4,7,6, 3, 13,14,10, 8 ]
print(a[6:])
print(verifyBST([8,3,1,6,4,7,10,14,13]))
