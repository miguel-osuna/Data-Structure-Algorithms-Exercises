# Recursive make change function
def recursionMakeChange(coinValueList, change):
    minCoins = change
    # Base Case
    if change in coinValueList:
        return 1
    # Recursive Case
    else:
        # Iterates over coins that are smaller than the value of cents
        for i in [coin for coin in coinValueList if coin < change]:
            numCoins = 1 + recursionMakeChange(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins


# Memoize make change function
def memoizeMakeChange(coinValueList, change, knownResults):
    minCoins = change
    # Base Case
    if change in coinValueList:
        return 1
    # Base Case
    elif knownResults[change] > 0:
        return knownResults[change]
    # Recursive Case
    else:
        # Iterates over coins that are smaller than the value of cents
        for i in [coin for coin in coinValueList if coin < change]:
            numCoins = 1 + \
                memoizeMakeChange(coinValueList, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
        return minCoins


# Dynamic Programming make change function
def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    # Iterates cent by cent until it gets to change
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        # Iterates over coins that are smaller or equal than the value of cents
        for i in [coin for coin in coinValueList if coin <= cents]:
            # Check for the smaller coin count
            if minCoins[cents - i] + 1 < coinCount:
                coinCount = minCoins[cents - i] + 1
                newCoin = i
        # Add the coin count and the new coin to the same cents
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin

    return minCoins[cents]


# Print coins used for some change
def printCoinsUsed(change, coinsUsed):
    coin = change
    coinList = []
    print("Coins used for {} cents are".format(coin))
    while coin > 0:
        coinList.append(coinsUsed[coin])
        coin -= coinsUsed[coin]
    print(coinList)


if __name__ == "__main__":
    coinValueList = [1, 5, 10, 25]
    change = 63

    # Recursive Make Change
    print("\nCoin list is {}".format(coinValueList))
    print("Coins returned for change of {} cents are {}".format(
        change, recursionMakeChange(coinValueList, change)))

    # Memoize Make Change
    knownResults = [0] * (change + 1)
    print(knownResults)
    print("\nCoin list is {}".format(coinValueList))
    print("Coins returned for change of {} cents are {}".format(
        change, memoizeMakeChange(coinValueList, change, knownResults)))

    # Dynamic Programming Make Change
    minCoins = [0] * (change + 1)
    coinsUsed = [0] * (change + 1)
    print("\nCoins returned for change of {} cents are {}".format(
        change, dpMakeChange(coinValueList, change, minCoins, coinsUsed)))
    printCoinsUsed(change, coinsUsed)
