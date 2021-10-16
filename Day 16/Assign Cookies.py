class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j=0
        c=0
        for i in g:
            if j==len(s):
                break
            while True:
                if j==len(s):
                    break
                if s[j]>=i:
                    j=j+1
                    c=c+1
                    break
                j=j+1
        return c  
