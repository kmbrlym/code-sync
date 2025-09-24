class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dct = {}
        for i in nums:
            if i in dct:
                dct[i] += 1
            else:
                dct[i]= 1
        for i in dct.keys():
            if dct[i] == 1:
                return i