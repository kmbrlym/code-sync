class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums:
            idx = abs(i) - 1
            if nums[idx] < 0:
                res.append(abs(i))
            nums[idx] = -nums[idx]
        return res