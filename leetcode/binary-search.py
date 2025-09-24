class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lst = nums
        idx = 0
        while lst:
            mid = len(lst) // 2
            if lst[mid] == target:
                return mid + idx
            elif len(lst) == 1:
                return -1
            elif lst[mid] < target:
                lst = lst[mid:]
                idx += mid
            else:
                lst = lst[:mid]
        return -1