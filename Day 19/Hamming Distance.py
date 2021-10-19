class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a=bin(min(x,y))[2:]
        b=bin(max(x,y))[2:]
        a=a.rjust(len(b),"0")
        c=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                c=c+1
        return c
                
