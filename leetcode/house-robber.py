class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 3)            
        for i in range(0, len(nums)):
            dp[i+3] = nums[i] + max(dp[i], dp[i+1])
        return max(dp[len(nums)+2], dp[len(nums)+1])