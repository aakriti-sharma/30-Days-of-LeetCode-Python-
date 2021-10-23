class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        s=0
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                s=s+i+num//i
        return num==s+1
