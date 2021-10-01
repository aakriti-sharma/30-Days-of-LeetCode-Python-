class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i1=0
        i2=0
        f=0
        for i in range (0,len(nums)):
            i1=i
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    i2=j
                    f=1
                    break
            if f==1:
                break
           
        return [i1,i2]
