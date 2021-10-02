class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        c=""
        f=1
        for j in range(0,len(strs[0])):
            for i in strs:
                if j>len(i)-1 :
                    f=0
                    break
                if i[j]!=strs[0][j]:
                    f=0
                    break
            if f==0:
                break
            else:
                c=c+strs[0][j]
        return c
