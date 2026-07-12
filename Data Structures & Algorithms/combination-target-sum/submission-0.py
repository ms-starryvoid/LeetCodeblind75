class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,curr,total):
            if total==target:
                return res.append(curr.copy())
            if total>target or i>=len(nums):
                return
            curr.append(nums[i])
            dfs(i,curr, total+nums[i])
            curr.pop()
            dfs(i+1,curr,total)
            return res
        return dfs(0,[],0)
