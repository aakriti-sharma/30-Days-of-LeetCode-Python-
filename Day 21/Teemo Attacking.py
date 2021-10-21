class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        t=0
        for i in range(len(timeSeries)-1):
            if timeSeries[i+1]-timeSeries[i]<duration:
                t=t+timeSeries[i+1]-timeSeries[i]
            else:
                t=t+duration
        return t+duration
