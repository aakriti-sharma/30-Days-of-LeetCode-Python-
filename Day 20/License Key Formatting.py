class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        while "-" in s:
            s=s.replace("-","")
        i=len(s)-1
        l=[]
        while i>k-1:
            l.append(s[i-k+1:i+1])
            i=i-k
        if i>=0:
            l.append(s[:i+1])
        return "-".join(l[::-1]).upper()
