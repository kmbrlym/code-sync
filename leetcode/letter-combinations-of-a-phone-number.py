import itertools

class Solution(object):
    def combin(self, letter, listy):
        res = []
        for i in listy:
            res.append(letter + i)
        return res

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dct = {'2':["a", "b", "c"], '3': ["d", "e", "f"], '4': ["g", "h", "i"], '5': ["j", "k", "l"], '6': ["m", "n", "o"], '7': ["p", "q", "r", "s"], '8': ["t", "u", "v"], '9':["w", "x", "y", "z"]}
        lst = []
        if len(digits) == 1:
            return dct[digits[0]]
        to_process = dct[digits[0]]
        i = 0
        while i < len(digits)-1:
            temp = []
            for j in to_process:
                temp.extend(self.combin(j, dct[digits[i+1]]))
                if i == len(digits) - 2:
                    lst.extend(self.combin(j, dct[digits[i+1]]))
            to_process = temp 
            i += 1
        return lst