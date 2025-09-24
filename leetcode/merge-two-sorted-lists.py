# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr1 = list1
        curr2 = list2
        dummy = ListNode(0)
        new_list = dummy
        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                new_list.next = curr1
                curr1 = curr1.next
            else:
                new_list.next = curr2
                curr2 = curr2.next
            new_list = new_list.next
        if curr1 is not None:
            new_list.next = curr1
        if curr2 is not None:
            new_list.next = curr2
        return dummy.next