
prices = [5, 10, 15, 20, 25, 25, 24, 21, 19, 20, 25, 28, 30, 30, 28, 18, 10]
test = [100, 9, 8, 7, 6, 5, 0, 10]


def trade(prices):
    return sum((prices[i+1]-prices[i] for i in range(len(prices[:-1])) if prices[i+1] >= prices[i]))

print trade(test)
print trade(prices)