def max_profit(prices):
    profit = []
    temp = prices[0] if prices else 0
    for index, value in enumerate(prices):
        if value <= temp:
            temp = value
        else:
            profit.append(value-temp)
    max_val = max(profit) if profit else 0
    return max_val


max_profit_value = max_profit([7, 6, 4, 3, 1])
print(max_profit_value)
