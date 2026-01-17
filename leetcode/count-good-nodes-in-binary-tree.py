# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = [[float('-inf'),root]]
        result = 1
        while q:
            next_level = []
            for i in q:
                temp = max(i[0],i[1].val)
                if i[1].left:
                    if i[1].left.val >= temp:
                        result += 1
                    next_level.append([temp, i[1].left])
                if i[1].right:
                    if i[1].right.val >= temp:
                        result += 1
                    next_level.append([temp, i[1].right])
                q = next_level
        return result