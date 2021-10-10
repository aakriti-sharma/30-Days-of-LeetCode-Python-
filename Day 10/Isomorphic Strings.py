class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
            j=0
            for i in s:
                l1=s.index(i)
                l2=t.index(t[j])
                j=j+1
                if l1!=l2:
                    return False
            return True
