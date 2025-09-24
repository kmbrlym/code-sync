# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        lst = []
        curr = head
        while curr is not None:
            lst.append(curr.val)
            curr = curr.next
        if len(lst) == 1:
            return True
        if len(lst) % 2 == 0:
            return lst[:len(lst)//2] == lst[len(lst)//2:][::-1]
        else:
            return lst[:len(lst)//2] == lst[len(lst)//2+1:][::-1]