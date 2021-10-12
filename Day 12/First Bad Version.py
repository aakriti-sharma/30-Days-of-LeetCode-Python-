# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        f=1
        l=n
        m=0
        while f<=l:
            m=(f+l)//2
            if isBadVersion(m):
                if not isBadVersion(m-1):
                    return m
                l=m-1
            else:
                f=m+1
            
