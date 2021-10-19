class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        l=len(s)//2+1
        z=[""]*l*numRows            #using 1D instead of 2D array saves some time but increases memory by 4 MB
        r=""
        i,j,k=0,0,1
        for d in s:
            z[i*l+j]=d
            if i==0:
                k=1
            if i<numRows-1 and k==1:
                i=i+1
                continue            #using continue instead of if-else saves time
            elif i==numRows-1 or k==0:
                k=0
                i=i-1
                j=j+1
                continue

        return "".join(z)
