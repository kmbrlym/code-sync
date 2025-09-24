class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst = []
        set_of_nums = [i for i in range(1,len(nums)+1)]
        return list(set(set_of_nums) - set(nums))