class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ln=len(nums)
        nums.sort()
        ans=[]
        for i in range(ln-1):
            l=i+1
            r=ln-1
            target=0-nums[i]
            while l<r:
                if nums[l]+nums[r]==target:
                    if [nums[l],nums[r],nums[i]] not in ans:
                        ans.append([nums[l],nums[r],nums[i]])
                    l+=1
                    r-=1
                elif nums[l]+nums[r]<target:
                    l+=1
                else:
                    r-=1
        return ans

        