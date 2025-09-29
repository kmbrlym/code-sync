# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        lst1 = []
        lst2 = []
        que = [p]
        que2 = [q]
        while que and que2:
            next1 = []
            next2 = []
            for item1, item2 in zip(que,que2):
                if item1:
                    lst1.append(item1.val)
                    next1.extend([item1.left, item1.right])
                else:
                    lst1.append(item1)
                if item2:
                    lst2.append(item2.val)
                    next2.extend([item2.left, item2.right])
                else:
                    lst2.append(item2)
            que = next1
            que2 = next2
        return lst1 == lst2