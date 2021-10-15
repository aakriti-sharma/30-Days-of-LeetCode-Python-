# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        f=0
        l=n
        while True:
            m=(f+l)//2
            if guess(m)==0:
                return m
            elif guess(m)<0:
                l=m-1
            else:
                f=m+1
