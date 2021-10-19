class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1+nums2             # + instead of .extend( ) saves time 
        nums1.sort()
        l=len(nums1)
        if l%2==1:                      # if-else instead of one line return statements saved ~100 ms
            return float(nums1[l//2])  
        else:
            return (nums1[l//2-1]+nums1[l//2])/2
