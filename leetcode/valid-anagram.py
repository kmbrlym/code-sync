from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = Counter(s)
        hash_t = Counter(t)
        set_s = set()
        for i in hash_s:
            set_s.add(i)
            if i in hash_t:
                if hash_t[i] != hash_s[i]:
                    return False
            else:
                return False
        set_t = set()
        for i in hash_t:
            set_t.add(i)
        return len(set_t) == len(set_s)