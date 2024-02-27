# 121. Best Time to Buy and Sell Stock


def maxProfit(prices: list[int]) -> int:
    if len(prices) < 2: return 0
    
    left   = 0 # buy
    right  = 1 # sell
    profit = 0
    
    while right < len(prices):
        buy    = prices[left]
        sell   = prices[right]
                
        if sell < buy:
            left = right
        else:
            profit = max(profit, sell - buy)
        
        right += 1

    return profit       
        

print(maxProfit([7,1,5,3,6,4])) # 5
print(maxProfit([7,6,4,3,1]))   # 0
