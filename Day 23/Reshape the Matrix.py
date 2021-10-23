class Solution:
    def matrixReshape(self, mat: List[List[str]], r: int, c: int) -> List[List[str]]:
        s=[]
        for i in mat:
            for j in i:
                s.append(j)
        print(s)
        l=[[0]*c for i in range(r)]
        if r*c!=len(s):
            return mat
        k=0
        for i in range(r):
            for j in range(c):
                l[i][j]=s[k]
                k=k+1
        return l
