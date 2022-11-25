'''
    104. 二叉树的最大深度
    给定一个二叉树，找出其最大深度。
    二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
    说明: 叶子节点是指没有子节点的节点。
    示例：
    给定二叉树 [3,9,20,null,null,15,7]，
        3
       / \
      9  20
        /  \
       15   7
    返回它的最大深度 3 。
    通过次数893,081提交次数1,158,500
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def my_bsf(root: TreeNode, output_list: []):
    queue = []
    queue.append(root)
    while queue:
        level = list()
        for i in range(len(queue)):
            tmp = queue.pop(0)
            level.append(tmp.val)
            if tmp.left is not None:
                queue.append(tmp.left)
            if tmp.right is not None:
                queue.append(tmp.right)
        output_list.append(level)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = []
        if root is None:
            return 0
        my_bsf(root, result)
        print(len(result))
        return len(result)