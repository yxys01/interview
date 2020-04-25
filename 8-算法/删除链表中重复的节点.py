'''
思路：准备一个字典，扫描到一个链表节点，将其作为key存到字典中，再次扫描
如果存在该节点，就忽略；不存在就保存
是一个新链表的过程
'''
# 新建一个类，表示节点
class LinkedNode:
    def __init__(self,x):
        self.val = x
        self.next = None
# 传入头指针
def deleteDuplication(pHead):
    nodeValues = {}
    # 新的头指针；最后直接返回它
    newHead = LinkedNode(pHead.val)
    # 将其添加到字典中，val作为字典的key
    nodeValues[pHead.val] = pHead.val
    # 保存新的头指针
    curNode = newHead

    # 扫描；读第二个
    while pHead.next:
        # 将第二个设为头指针
        pHead = pHead.next
        # 如果nodeValues中不存在pHead.val
        if nodeValues.get(pHead.val) == None:
            # 创建一个新节点连接到后面
            curNode.next = LinkedNode(pHead.val)
            curNode = curNode.next
            # 将当前值存到字典中，以便下次查找
            nodeValues[pHead.val] = pHead.val
    return newHead

header = LinkedNode(5)
node1 = LinkedNode(5)
header.next = node1
node2 = LinkedNode(10)
node1.next = node2
node3 = LinkedNode(4)
node2.next = node3

# 打印链表的函数
def printLinker(header):
    p = header
    while p:
        print(p.val)
        p = p.next

header = deleteDuplication(header)
printLinker(header)