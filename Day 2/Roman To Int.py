class Solution:
    def romanToInt(self, s: str) -> int:
        r=['I','V','X','L','C','D','M']
        v=[1,5,10,50,100,500,1000]
        e=0
        for i in range(0,len(s)):
            a=s[i]            
            n=v[r.index(a)]           
            if i==len(s)-1:
                e=e+n
                break
            else:
                 m=v[r.index(s[i+1])]
            if n<m:
                e=e-n
            else:
                e=e+n
        return e
