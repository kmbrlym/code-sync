# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        curr = head
        length = 0
        while curr is not None:
            length += 1
            curr = curr.next
        idx = length - n - 1
        if n == length:
            return head.next
        curr = head
        curr_idx = 0
        while curr is not None:
            if curr_idx == idx:
                curr.next = curr.next.next
            curr_idx += 1
            curr = curr.next
        return head