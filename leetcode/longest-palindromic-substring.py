class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        resL = 0
        resR = 0
        resLen = 0
        for i in range(len(s)):
            l, r = i, i
            while l>= 0 and r<len(s) and s[l] == s[r]:
                    if (r-l+1) > resLen:
                        resLen = r-l+1
                        resL = l
                        resR = r
                    l -= 1
                    r += 1
            l, r = i, i+1
            while l>= 0 and r<len(s) and s[l] == s[r]:
                    if (r-l+1) > resLen:
                        resLen = r-l+1
                        resL = l
                        resR = r
                    l -= 1
                    r += 1
        return s[resL:resR+1]