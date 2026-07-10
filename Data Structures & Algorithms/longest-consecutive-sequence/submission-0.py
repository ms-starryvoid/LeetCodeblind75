class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length=0
        for i in range(len(nums)):
            if nums[i]-1 in nums:
                continue
            else:
                l=1
                j=nums[i]+1

                while j in nums:
                    l+=1
                    j+=1
                if l>length:
                    length=l
        return length
        