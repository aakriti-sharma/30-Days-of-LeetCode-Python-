class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d=""
        if s=="":
            return t            
        s=sorted(s)
        t=sorted(t)   
        for i in t:            
            if i in s:
                s.remove(i)
            else:
                d=d+i 
        return d
