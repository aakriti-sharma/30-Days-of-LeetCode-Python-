class Solution:
    def isPalindrome(self, x: int) -> bool:
        r=0
        a=0
        y=x
        if x<0:
            return False
        while x>0:
            a=x%10
            r=r*10+a
            x=x//10
        if r==y:
            return True
        return False
