class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        if n==0:
            return True
        if len(flowerbed)==1:
            if c>1 or flowerbed[0]==1:
                return False
            return True
        if flowerbed[0]==0 and flowerbed[1]==0:
            flowerbed[0]=1
            c=c+1
        if flowerbed[-1]==0 and flowerbed[-2]==0:
            flowerbed[-1]=1
            c=c+1
        if c>=n:
            return True
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
                flowerbed[i]=1
                c=c+1
            if c>=n:
                return True
        return False
