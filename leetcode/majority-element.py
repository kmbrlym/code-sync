class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dct = {}
        for i in nums:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        max_val = 0
        max_key = None
        for key,val in dct.items():
            if val > max_val:
                max_val = val
                max_key = key
        return max_key