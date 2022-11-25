'''
    102. 二叉树的层序遍历
    给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
    示例 1：
    输入：root = [3,9,20,null,null,15,7]
    输出：[[3],[9,20],[15,7]]
    示例 2：
    输入：root = [1]
    输出：[[1]]
    示例 3：
    输入：root = []
    输出：[]
    提示：
    树中节点数目在范围 [0, 2000] 内
    -1000 <= Node.val <= 1000
'''

# 节点类
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        my_bsf(root, result)
        # print(result)
        return result