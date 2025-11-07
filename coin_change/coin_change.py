def calculate_minimum_coins(coins, remaining_amount, counter):
    if remaining_amount < 0:
        return -1
    if remaining_amount == 0:
        return 0
    if counter[remaining_amount - 1] != float('inf'):
        return counter[remaining_amount - 1]
    minimum = float('inf')

    for s in coins:
        result = calculate_minimum_coins(coins, remaining_amount - s, counter)
        if result >= 0 and result < minimum:
            minimum = 1 + result

    counter[remaining_amount - 1] =  minimum if minimum !=  float('inf') else  -1
    return counter[remaining_amount - 1]

def coin_change(coins, total):
    if (total < 1):
        return 0
    counter = (total + 1) *[total + 1]
    counter[0] = 0

    for i in range (total + 1):
        for coin in coins:
            if (i >= coin):
                counter[i] = min(counter[i], (counter[i-coin] + 1))
    if (counter[total] > total):
        return -1
    else:
        return (counter[total])

 #Driver Code

def main():

    coins = [[1, 3, 4, 5], [1, 4, 6, 9], [6, 7, 8], [1, 2, 3, 4, 5], [14, 15, 18, 20]]
    total = [7, 11, 27, 41, 52]

    for i in range(len(total)):
        print(str(i+1) + ".\tThe minimum number of coins required to find " + str(total[i]) + " from " + str(coins[i]) + " is: " + str(coin_change(coins[i], total[i])))
        print("-" * 100)

if __name__ == '__main__':
    main()
