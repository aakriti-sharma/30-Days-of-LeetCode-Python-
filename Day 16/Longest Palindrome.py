class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s)
        l=0
        f=0
        for v in c.values():
            if v%2==0:
                l=l+v
            else:
                f=1
                l=l+v-1
        if f==1:
            return l+1
        return l
