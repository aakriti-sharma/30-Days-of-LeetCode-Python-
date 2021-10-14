class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,len(nums)):
            if nums[i]!=i:
                return i
        return nums[-1]+1
