class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue= float ('inf')
        maxValue= 0
        for i in prices:
            if i < minValue:
                minValue= i
            
            profit = i - minValue

            if profit> maxValue:
                maxValue=profit

        return maxValue