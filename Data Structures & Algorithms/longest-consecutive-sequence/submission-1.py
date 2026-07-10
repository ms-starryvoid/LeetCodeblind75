class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length=0
        n_set=set(nums)
        for i in range(len(nums)):
            if nums[i]-1 in n_set:
                continue
            else:
                l=1
                j=nums[i]+1
                while j in n_set:
                    l+=1
                    j+=1
                if l>length:
                    length=l
        return length
        