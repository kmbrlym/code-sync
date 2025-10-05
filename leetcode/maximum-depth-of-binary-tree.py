# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, root, depth):
        if not root:
            return depth
        else:
            return max(self.dfs(root.left, depth + 1), self.dfs(root.right, depth + 1))

    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.dfs(root, 0)