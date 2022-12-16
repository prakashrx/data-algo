def max_profit(stock_prices):
    if not stock_prices or len(stock_prices) < 2:
        return 0

    arr  =  [ stock_prices[i+1] - stock_prices[i]  for i in range(len(stock_prices) - 1) ]
    s = [0] * len(arr)
    s[0] = arr[0]
    for i in range(1, len(arr)):
        s[i] = max(arr[i], s[i-1] + arr[i])
    return max(0, max(s))


print(max_profit([10, 4, 11, 1, 5]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([]))


# -6, 7, -10, 4
