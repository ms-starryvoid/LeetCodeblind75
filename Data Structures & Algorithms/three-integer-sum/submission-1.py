class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ln=len(nums)
        nums.sort()
        ans=[]
        for i in range(ln-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l=i+1
            r=ln-1
            target=0-nums[i]
            while l<r:
                if nums[l]+nums[r]==target:
                    ans.append([nums[l],nums[r],nums[i]])
                    l+=1
                    r-=1
                    while l< r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif nums[l]+nums[r]<target:
                    l+=1
                else:
                    r-=1
        return ans

        