class Solution(object):
    def checkPalindrome(self, string):
        n = len(string)
        mid = n // 2
        if n % 2 == 0:  # even length
            return string[:mid] == string[mid:][::-1]
        else:  # odd length
            return string[:mid] == string[mid+1:][::-1]

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [1] * len(s)
        for i in range(1, len(s)):
            for j in range(0, i):
                if self.checkPalindrome(s[j:i+1]):
                    dp[i] += 1
        return sum(dp)