# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        def helper(root, targetSum, lst):
            if not root:
                return []
            if not root.left and not root.right:
                if root.val == targetSum:
                    return [lst + [root.val]]
                return []
            left = helper(root.left, targetSum - root.val, lst+[root.val])
            right = helper(root.right, targetSum-root.val, lst+[root.val])
            return left + right
        return helper(root, targetSum, [])