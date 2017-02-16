
prices = [5, 10, 15, 20, 25, 25, 24, 21, 19, 20, 25, 28, 30, 30, 28, 18, 10]
test = [100, 9, 8, 7, 6, 5, 0, 10]


def trade(prices):
    return sum(map(lambda v: prices[v+1]-prices[v], filter( lambda u: prices[u+1] > prices[u], range(len(prices[:-1])))))

print trade(test)
print trade(prices)