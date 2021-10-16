class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1=Counter(ransomNote)
        c2=Counter(magazine)
        for k,v in c1.items():
            if k not in c2.keys():
                return False
            if c2[k]<v:
                return False
        return True
