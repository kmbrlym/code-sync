class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def backtract(front, back, par):
            if front == back == n:
                res.append(par)
            if front < n:
                backtract(front+1, back, par + "(")
            if back < front:
                backtract(front, back+1, par + ")")
        backtract(0,0,"")
        return res