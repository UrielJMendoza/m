class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfits = []
        left = 0
        ##so if prices at left is less then prices at right append 

        for right in range(len(prices)):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfits.append(profit)

            
            else:
                left = right
                right += 1

        if not maxProfits:
            return 0


        return max(maxProfits)