class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        c=Counter(nums)
        f,s,t=0,0,0
        for m,v in c.items():
            t=v-2
            if v>=2:
                f=nums.index(m)
                s=nums[f+1:].index(m)+f+1
                print(f)
                print(s)
                if (s-f)<=k:
                    return True
                else:
                    while t>0:
                        f=s
                        s=nums[f+1:].index(m)+f+1
                        if (s-f)<=k:
                            return True
                        t=t-1
        return False
