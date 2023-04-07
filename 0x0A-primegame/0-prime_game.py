#!/usr/bin/python3
'''Prime game module.
'''
def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_game(n):
        primes = get_primes(n)
        maria_turn = True
        while primes:
            if maria_turn:
                for prime in primes:
                    if n % prime == 0:
                        primes.remove(prime)
                        break
                else:
                    return "Ben"
            else:
                for prime in primes:
                    if n % prime == 0:
                        primes.remove(prime)
                        break
                else:
                    return "Maria"
            maria_turn = not maria_turn
        return "Maria"

    winners = {"Maria": 0, "Ben": 0}
    for n in nums:
        winner = play_game(n)
        winners[winner] += 1

    if winners["Maria"] > winners["Ben"]:
        return "Maria"
    elif winners["Ben"] > winners["Maria"]:
        return "Ben"
    else:
        return None

