class Solution:
    def isPalindrome(self, s: str) -> bool:
        mew = ""
        for i in s:
            if i.isalnum():
                mew += i
        mew = mew.lower()
        return mew == mew[::-1]