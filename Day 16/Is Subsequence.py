class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l=[0]
        for i in s:
            if i not in t:
                return False
            j=t.index(i)
            l.append(j+l[-1])
            t=t[j+1:]
            print(t)
            print(l)
        return l==sorted(l)
