class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window = sum(nums[:k])
        max_sum = window
        for i in range(k, len(nums)):
            window += nums[i] - nums[i-k]
            if window > max_sum:
                max_sum = window
        return max_sum / float(k)