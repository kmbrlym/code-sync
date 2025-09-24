class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        biggest_diff = 0
        min_so_far = min(prices[:1])
        for i in range(1, len(prices)):
            if min_so_far > prices[i]:
                min_so_far = prices[i]
            curr_diff = prices[i] - min_so_far
            if curr_diff > biggest_diff:
                biggest_diff = curr_diff
        return biggest_diff