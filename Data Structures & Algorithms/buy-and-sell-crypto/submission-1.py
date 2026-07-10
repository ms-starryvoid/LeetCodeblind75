class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #the maximum margin
        maxp=0
        minprice=prices[0]
        for price in prices:
            p=price-minprice
            maxp=max(p,maxp)
            minprice=min(minprice,price)
        return maxp
            