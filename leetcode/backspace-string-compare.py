class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def check(string):
            stack = []
            for i in string:
                if i != "#":
                    stack.append(i)
                elif stack:
                    stack.pop()
            return stack
        return check(s) == check(t)