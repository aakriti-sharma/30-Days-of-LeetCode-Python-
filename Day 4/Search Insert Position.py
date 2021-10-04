class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        while nums[i]<target:
            i=i+1
            if i==len(nums):
                break
        return i
