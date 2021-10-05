class Solution:
    def climbStairs(self, n: int) -> int:
        c=0
        for x in range(0,n+1):
            for y in range(0,n//2+1):
                if 2*y+x==n:
                    if x==0 or y==0:
                        c=c+1
                    else:
                        c=c+math.factorial(x+y)/(math.factorial(x)*math.factorial(y))                    
        return int(c)
