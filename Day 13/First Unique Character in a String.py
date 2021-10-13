class Solution:
    def firstUniqChar(self, s: str) -> int:
        f=Counter(s)
        for k,v in f.items():
            if v==1:
                return s.index(k)
        return -1
