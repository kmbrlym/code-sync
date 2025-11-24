class Solution(object):
    from collections import Counter
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # the idea is to use heap, always get the one with the highest counter value
        # but when appending it to the resulting string,
        # don't use the character you previously used
        # to do this, you have to hold the popped heap value 
        # and only push it to heap in the next iteration
        res, c = "", Counter(s)
        pq = [(-value, key) for key, value in c.items()]
        heapq.heapify(pq)
        p_a, p_b = 0, ""
        while pq:
            a, b = heapq.heappop(pq)
            res += b
            if p_a < 0:
                heapq.heappush(pq, (p_a, p_b))
            a += 1
            p_a, p_b = a, b
        if len(s) != len(res):
            return ""
        return res