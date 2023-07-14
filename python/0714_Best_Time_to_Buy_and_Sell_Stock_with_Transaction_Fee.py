class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit_holding_stock = -prices[0]
        profit_without_stock = 0

        for i in range(1, len(prices)):
            tmp = profit_holding_stock
            profit_holding_stock = max(profit_holding_stock, profit_without_stock - prices[i])
            profit_without_stock = max(profit_without_stock, tmp + prices[i] - fee)
        return profit_without_stock
