
prices = [5, 10, 15, 20, 25, 25, 24, 21, 19, 20, 25, 28, 30, 30, 28, 18, 10]
test = [100, 9, 8, 7, 6, 5, 0, 10]


def trade(prices):
    result = 0

    for i in range(len(prices[:-1])):
        curr = prices[i]
        next = prices[i+1]

        if next >= curr:
            result += next - curr

    return result

# def trade2(prices):
#     for i, v in enumerate(prices):


print trade(test)
print trade(prices)