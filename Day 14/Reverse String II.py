class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<k:
            return "".join(reversed(s))
        c=""
        if len(s)<2*k:
            return "".join(reversed(s[0:k]))+s[k:]
        i=0
        while i<len(s):
            c=c+"".join(reversed(s[i:i+k]))+s[i+k:i+2*k]
            i=i+2*k
        return c
