class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        curr = s
        for i in t:
            if not curr:
                return True
            if curr[0] == i:
                curr = curr[1:]
        return not curr