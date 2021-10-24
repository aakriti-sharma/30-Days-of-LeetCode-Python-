class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s=n*(n+1)//2
        return [sum(nums)-sum(set(nums)),s-sum(set(nums))]
