class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f="qwertyuiop"
        s="asdfghjkl"
        t="zxcvbnm"
        r=[]
        for w in words:
            o=0
            i=list(set(w.lower()))
            if i[0] in f:
                for k in i:
                    if k not in f:
                        o=1
                if o==0:
                        r.append(w)
            elif i[0] in s:
                for k in i:
                    if k not in s:
                        o=1
                if o==0:
                       r.append(w)
            elif i[0] in t:
                for k in i:
                    if k not in t:
                        o=1
                if o==0:
                        r.append(w)
        return r
                
