class Solution:
    def isHappy(self, n: int) -> bool:
        r=[]
        while True:
            l=list(map(int,str(n).strip("")))
            n=sum([i**2 for i in l])
            if n==1:
                return True
            elif n in r:
                return False
            else:
                r.append(n)
            
