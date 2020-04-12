def recursion_make_change(coin_value_list, change):
    """ Recursive make change function"""
    min_coins = change
    # Base Case
    if change in coin_value_list:
        return 1
    # Recursive Case
    else:
        # Iterates over coins that are smaller than the value of cents
        for i in [coin for coin in coin_value_list if coin < change]:
            num_coins = 1 + recursion_make_change(coin_value_list, change - i)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


def memoize_make_change(coin_value_list, change, know_results):
    """ Memoize make change function """
    min_coins = change
    # Base Case
    if change in coin_value_list:
        return 1
    # Base Case
    elif know_results[change] > 0:
        return know_results[change]
    # Recursive Case
    else:
        # Iterates over coins that are smaller than the value of cents
        for i in [coin for coin in coin_value_list if coin < change]:
            num_coins = 1 + memoize_make_change(
                coin_value_list, change - i, know_results
            )
            if num_coins < min_coins:
                min_coins = num_coins
                know_results[change] = min_coins
        return min_coins


def dp_make_change(coin_value_list, change, min_coins, coins_used):
    """ Dynamic programming make change function """

    # Iterates cent by cent until it gets to change
    for cents in range(change + 1):
        coin_count = cents
        newCoin = 1
        # Iterates over coins that are smaller or equal than the value of cents
        for i in [coin for coin in coin_value_list if coin <= cents]:
            # Check for the smaller coin count
            if min_coins[cents - i] + 1 < coin_count:
                coin_count = min_coins[cents - i] + 1
                newCoin = i
        # Add the coin count and the new coin to the same cents
        min_coins[cents] = coin_count
        coins_used[cents] = newCoin

    return min_coins[cents]


def print_coins_used(change, coins_used):
    """" Print coins used for some change """

    coin = change
    coin_list = []
    print("Coins used for {} cents are".format(coin))
    while coin > 0:
        coin_list.append(coins_used[coin])
        coin -= coins_used[coin]
    print(coin_list)


def main():
    coin_value_list = [1, 5, 10, 25]
    change = 63

    # Recursive Make Change
    print("\nCoin list is {}".format(coin_value_list))
    print(
        "Coins returned for change of {} cents are {}".format(
            change, recursion_make_change(coin_value_list, change)
        )
    )

    # Memoize Make Change
    know_results = [0] * (change + 1)
    print(know_results)
    print("\nCoin list is {}".format(coin_value_list))
    print(
        "Coins returned for change of {} cents are {}".format(
            change, memoize_make_change(coin_value_list, change, know_results)
        )
    )

    # Dynamic Programming Make Change
    min_coins = [0] * (change + 1)
    coins_used = [0] * (change + 1)
    print(
        "\nCoins returned for change of {} cents are {}".format(
            change, dp_make_change(coin_value_list, change, min_coins, coins_used)
        )
    )
    print_coins_used(change, coins_used)


if __name__ == "__main__":
    main()
