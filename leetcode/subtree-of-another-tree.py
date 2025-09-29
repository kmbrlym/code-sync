# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def serialize(self,root):
        if not root:
            return "X"
        return "#" + str(root.val) + self.serialize(root.left) + self.serialize(root.right)
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        r = self.serialize(root)
        s = self.serialize(subRoot)
        return s in r