def max_profit(prices):
    num_prices = len(prices)
    if (num_prices < 2):
        return 0
    if (num_prices == 2 and prices[1] > prices[0]):
        return (prices[1] - prices[0])
        
    buyIndex = 0
    sellIndex = 1
    maxProfit = 0
    
    for i in range(num_prices):
        cur_price = prices[i]
        #print("index cur_price buy_Price max_profit ", i, cur_price, prices[buyIndex], maxProfit)
        if (cur_price > prices[buyIndex]):
            maxProfit = max(maxProfit, cur_price - prices[buyIndex])
        else:
            buyIndex = i
    return maxProfit

# Driver code
def main():
    prices = [
                [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9],
                [8, 2, 6, 4, 7, 5],
                [7, 6, 4, 3, 1],
                [2, 6, 8, 7, 8, 7, 9, 4, 1, 2, 4, 5, 8],
                [1, 2]
             ]

    for i in range(len(prices)):
        print(i + 1, ". Stock prices = ", prices[i], sep="")
        print("   Maximum profit = ", max_profit(prices[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
