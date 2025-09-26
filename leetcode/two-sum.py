class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            temp = target - nums[i]
            if temp in hashmap:
                idx = hashmap[temp]
                if idx != i:
                    return [i, idx]