# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(r):
            if not r:
                return [True, 0]
            left = dfs(r.left)
            right = dfs(r.right)
            balanced = [left[0] and right[0] and abs(left[1]-right[1])<=1,  1+ max(left[1], right[1])]
            return balanced
        return dfs(root)[0]