# 二叉树
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
# root根节点；路径之和=n
def findPath(root,n):
    if not root:
        return []
    # 最终结果；可以没有路径，也可能是一条或多条路径
    result = []
    # root根节点；path路径；当前和
    # 迭代
    def findPath2(root,path,currentNum):
        # 当前和
        currentNum += root.val
        path.append(root)
        # 判断root是否为叶子节点;只有左子树和右子树都为空的时候为叶子节点
        flag = root.left == None and root.right ==None
        # 如果当前值=n，且为叶子节点，返回路径
        if currentNum == n and flag:
            onepath = []
            for node in path:
                onepath.append(node.val)
            result.append(onepath)
        # 如果当前值<n，继续递归
        if currentNum < n:
            # 对左子树递归
            if root.left:
                findPath2(root.left, path, currentNum)
            if root.right:
                findPath2(root.right, path, currentNum)
        # 处理完后，将path弹出，继续从上一个节点重新递归
        path.pop()
    findPath2(root,[],0) # 干啥的？
    return result

root = TreeNode(10)
left = TreeNode(6)
right = TreeNode(15)

root.left = left
root.right = right

left1 = TreeNode(11)
right1 = TreeNode(20)

right.left = left1
right.right = right1

left2 = TreeNode(9)
left1.left = left2

'''
                    10
                6       15
                     11    20
                    9
'''
print(findPath(root,16))
print(findPath(root,45))