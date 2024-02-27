# 121. Best Time to Buy and Sell Stock


def maxProfit(prices: list[int]) -> int:
    if len(prices) < 2: return 0
    cheap_buy  = prices[0]
    max_profit = 0
    for i in range(len(prices) - 1):
        buy = prices[i]
        if i != 0 and buy >= cheap_buy:
            continue
        else:
            cheap_buy = buy
            expen_sell = prices[i + 1]
        for j in range(i, len(prices)):
            sell = prices[j]
            if j != 1 and sell < expen_sell:
                continue
            else:
                expen_sell = sell
            if expen_sell <= cheap_buy:
                continue
            else:
                max_profit = max(max_profit, sell - buy)
    return max_profit


print(maxProfit([7,1,5,3,6,4])) # 5
print(maxProfit([7,6,4,3,1]))   # 0
