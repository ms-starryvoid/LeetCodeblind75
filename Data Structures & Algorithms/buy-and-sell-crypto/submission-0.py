class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #the maximum margin
        maxp=0
        for i in range(len(prices)-1):
            j=i+1
            while j< len(prices):
                p=prices[j] - prices[i]
                maxp=max(p,maxp)
                j+=1
        return maxp