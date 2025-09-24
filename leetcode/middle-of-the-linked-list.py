# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        dct = {}
        i = 0
        while curr is not None:
            dct[i] = curr
            i += 1
            curr = curr.next
        mid_idx = i // 2
        return dct[mid_idx]