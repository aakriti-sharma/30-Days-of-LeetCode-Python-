class Solution:
    def reverse(self, x: int) -> int:
        r=0
        a=0
        s=0
        if x<0:
            x=x*(-1)
            s=1
        while x>0:
            a=x%10
            r=r*10+a
            x=x//10
        if s==1:
            r=r*(-1)
        if -(2**31) <= r <= (2**31 - 1):
            return r
        else:
            return 0
            
