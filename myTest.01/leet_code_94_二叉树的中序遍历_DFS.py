'''
    94. 二叉树的中序遍历 DFS
    给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
    示例 1：
    输入：root = [1,null,2,3]
    输出：[1,3,2]
    示例 2：
    输入：root = []
    输出：[]
    示例 3：
    输入：root = [1]
    输出：[1]
    提示：
    树中节点数目在范围 [0, 100] 内
    -100 <= Node.val <= 100
'''

# 节点类
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(node: TreeNode, rlist: []):
    if node is not None:
        dfs(node.left, rlist)
        rlist.append(node.val)
        dfs(node.right, rlist)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        dfs(root, result)
        print(result)
        return result

