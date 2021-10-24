class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ls=[]
        lt=[]
        for i in s:
            if i=="#":
                if len(ls)>0:
                    ls.pop()
            else:
                ls.append(i)
        for i in t:
            if i=="#":
                if len(lt)>0:
                    lt.pop()
            else:
                lt.append(i)
        return ls==lt
        
