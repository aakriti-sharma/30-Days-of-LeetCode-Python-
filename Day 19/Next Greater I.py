class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[-1]*len(nums1)
        j=0
        for i in range(0,len(nums1)):
            j=nums2.index(nums1[i])
            for x in nums2[j:]:
                if x>nums1[i]:
                    l[i]=x
                    break
        return l
