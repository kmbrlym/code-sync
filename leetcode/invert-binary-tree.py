# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        q = [root]
        while q:
            next_level = []
            for i in q:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
                i.left, i.right = i.right, i.left
            q = next_level
        return root