def isWinner(x, nums):
    """
    Determine the winner of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list of int): Array of n for each round.

    Returns:
        str or None: "Maria" if she wins the most rounds,
        "Ben" if he wins the most,
                     or None if they tie.
    """
    if x <= 0 or not nums:
        return None

    # Precompute prime numbers up to the maximum n in nums
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    # Count wins for each player
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n, primes):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def sieve_of_eratosthenes(max_num):
    """
    Generate a list indicating prime numbers
    up to max_num using the Sieve of Eratosthenes.

    Args:
        max_num (int): The maximum number to check for primes.

    Returns:
        list of bool: A list where index i is True
        if i is a prime number, otherwise False.
    """
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    return primes


def play_game(n, primes):
    """
    Simulate a single round of the prime game.

    Args:
        n (int): The upper limit of the set of numbers (1 to n).
        primes (list of bool): Precomputed list of prime indicators.

    Returns:
        bool: True if Maria wins, False if Ben wins.
    """
    # Use a set to track available numbers
    available = set(range(1, n + 1))
    turn = 0  # Maria's turn is 0, Ben's turn is 1

    while True:
        # Find the next available prime
        next_prime = None
        for num in available:
            if primes[num]:
                next_prime = num
                break

        # If no primes are left, the current player loses
        if next_prime is None:
            return turn == 1  # Return True if Maria wins, False if Ben wins

        # Remove the prime and its multiples
        to_remove = set(range(next_prime, n + 1, next_prime))
        available -= to_remove

        # Switch turns
        turn = 1 - turn
