class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = 1
        zero_exists = 0
        for i in nums:
            if i == 0:
                zero_exists += 1
            else:
                prod = prod * i
        res = []
        for j in nums:
            if zero_exists == 0:
                res.append(prod/j)
            elif zero_exists == 1:
                if j == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(0)
        return res