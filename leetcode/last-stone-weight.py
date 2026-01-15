class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        c = [-i for i in stones]
        heapq.heapify(c)
        while len(c) >= 2:
            first= heapq.heappop(c)
            print(first)
            second = heapq.heappop(c)
            print(second)
            remaining = abs(first) - abs(second)
            if remaining > 0:
                heapq.heappush(c, -remaining)
        if c:
            return abs(c[0])
        return 0