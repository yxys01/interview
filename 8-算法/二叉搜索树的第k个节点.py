'''

中序遍历：遍历完后出来的就是排序好的列表

按中序遍历得到列表，在寻找第k个节点
'''

class TreeNode:
    def __init__(self,x):
        self.val = x
        # 左子树
        self.left = None
        # 右子树
        self.right = None
# 得到第k个节点
class KNode:
    # 传入根节点，第k个
    def kthNode(self,pRoot,k):
        # 全局变量
        global result
        result = []
        # 得到中序遍历的列表
        middle = self.midorder(pRoot)
        if k <= 0 or len(middle) < k:
            return None
        else:
            return middle[k - 1]
    # 中序遍历;传入根节点
    def midorder(self,pRoot):
        if not pRoot:
            return []
        # 递归；先中序左子树
        self.midorder(pRoot.left)
        # 访问根节点
        result.append(pRoot)
        # 中序右子树
        self.midorder(pRoot.right)
        return result

# 创建一个二叉搜索树，根节点10
root = TreeNode(10)
left = TreeNode(6)
right = TreeNode(15)
root.left = left
root.right = right

left1 = TreeNode(11)
right1 = TreeNode(20)

right.left = left1
right.right = right1

print(KNode().kthNode(root,3).val)