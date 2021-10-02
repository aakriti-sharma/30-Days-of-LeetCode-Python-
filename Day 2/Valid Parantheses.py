class Solution:
    def isValid(self, s: str) -> bool:
        b=[]
        for i in s:
            if i in ['(','{','[']:
                b.append(i)
            elif b==[]:
                return False
            elif i==')':
                if b[-1]=='(':
                    del b[-1]
                else:
                    break
            elif i==']':
                if b[-1]=='[':
                    del b[-1]
                else:
                    break  
            elif i=='}':
                if b[-1]=='{':
                    del b[-1]
                else:
                    break
        return b==[] 
