class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        curr = n
        while curr not in visit:
            total = 0
            for i in str(curr):
                total += int(i) ** 2
            if total == 1:
                return True
            visit.add(curr)
            curr = total
        return False