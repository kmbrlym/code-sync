# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        s = set()
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr is not None:
            if curr.val in s:
                prev.next = curr.next
            else:
                prev = prev.next
            s.add(curr.val)
            curr = curr.next
        return dummy.next