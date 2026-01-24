class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx = {}
        for i in range(len(numbers)):
            if numbers[i] not in idx:
                idx[numbers[i]] = i
            remaining = target - numbers[i]
            if remaining in idx and idx[remaining] != i:
                return [idx[remaining]+1, i+1]