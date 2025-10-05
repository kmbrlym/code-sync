class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original) != m * n:
            return []
        res = []
        temp = []
        for i in original:
            temp.append(i)
            if len(temp) == n:
                res.append(temp)
                temp = []
        return res