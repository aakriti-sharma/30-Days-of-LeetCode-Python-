class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p=""
        p1=""
        u=97
        e=[]
        e1=[]
        s=s.split(" ")
        if len(s)!=len(pattern):
            return False
        for i in s:
            if i in e:
                p=p+chr(e.index(i)+97)
            else:
                e.append(i)
                p=p+chr(e.index(i)+97)
        if p==pattern:
            return True 
        for i in pattern:
            if i in e1:
                p1=p1+chr(e1.index(i)+97)
            else:
                e1.append(i)
                p1=p1+chr(e1.index(i)+97)    
        return p==p1
            
