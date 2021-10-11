class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        p=math.trunc(math.log(n,2)*10000000000)/10000000000.0
        print(p)
        return p==p//1
