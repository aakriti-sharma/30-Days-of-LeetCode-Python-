class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            l=list(map(int,str(num)))
            if len(l)==1:
                return l[0]
            num=sum(l)
