#!/usr/bin/python3
"""
An implementation of the prime game program
"""


def isWinner(x, nums):
    """
    A function that implements the prime game

    This game is played between Ben and Maria
    """

    players_score = {'Ben': 0, 'Maria': 0}

    if not isinstance(nums, list):
        return None
    if len(nums) > x:
        return None
    if x == 0:
        return 'Ben'
    for i in range(x):
        numbers = [num for num in range(2, nums[i] + 1, 1)]
        loop_count = 0
        while (numbers):
            present = numbers.pop(0)
            numbers = [n for n in numbers if n % present != 0]
            loop_count += 1
        if loop_count % 2 == 0:
            players_score['Ben'] += 1
        else:
            players_score['Maria'] += 1
    if players_score['Ben'] > players_score['Maria']:
        return 'Ben'
    elif players_score['Maria'] > players_score['Ben']:
        return 'Maria'
    else:
        return None
