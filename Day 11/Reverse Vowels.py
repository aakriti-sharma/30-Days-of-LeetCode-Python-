cclass Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        idx=[]
        v=[]
        for i in range(0,len(s)):
            if s[i] in vowels:
                idx.append(i)
        l=[]
        l[:0]=s
        s=""
        for j in range(0,len(idx)//2):
            i=idx[j]
            k=idx[-(j+1)]
            l[i],l[k]=l[k],l[i]
        return s.join(l)
