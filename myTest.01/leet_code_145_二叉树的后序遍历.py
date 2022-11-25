'''
    145. 二叉树的后序遍历
    给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。
    示例 1：
    输入：root = [1,null,2,3]
    输出：[3,2,1]
    示例 2：
    输入：root = []
    输出：[]
    示例 3：
    输入：root = [1]
    输出：[1]
    提示：
    树中节点的数目在范围 [0, 100] 内
    -100 <= Node.val <= 100
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 节点类
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def postorder_fs(node: TreeNode, rlist: []):
    if node is not None:
        postorder_fs(node.left, rlist)
        postorder_fs(node.right, rlist)
        rlist.append(node.val)

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        postorder_fs(root, result)
        print(result)
        return result