# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        temp = []
        while curr is not None:
            temp.append(curr.val)
            curr = curr.next
        curr = head
        i = len(temp) - 1
        while curr is not None:
            curr.val = temp[i]
            curr = curr.next
            i -= 1
        return head