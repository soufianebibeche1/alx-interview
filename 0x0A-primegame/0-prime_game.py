#!/usr/bin/python3
"""

Prime game implementation
"""

def isWinner(x, nums):
    """
    Determines the overall winner after x rounds of the game.
    :param x: Number of rounds
    :param nums: List of n values for each round
    :return: Name of the player with the most wins ("Maria" or "Ben"), or None if tied
    """
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        available = set(range(1, n + 1))
        turn = 0

        while True:
            found_prime = False
            for num in available:
                if primes[num]:
                    found_prime = True
                    multiples = set(range(num, n + 1, num))
                    available -= multiples
                    break

            if not found_prime:
                if turn == 0:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            turn = 1 - turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
