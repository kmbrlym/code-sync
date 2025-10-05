# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDepth(self, node, depth, depths):
        if not node:
            return 0
        if not node.left and not node.right:
            depths.append(depth)
        self.findDepth(node.left, depth + 1, depths)
        self.findDepth(node.right, depth + 1, depths)
        return depths
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        depths = []
        return min(self.findDepth(root, 1, depths))