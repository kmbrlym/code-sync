class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mandatory_nums = [i for i in range(1, len(nums)+1)]
        missing_num = list(set(mandatory_nums) - set(nums))
        if missing_num:
            return missing_num[0]
        return 0