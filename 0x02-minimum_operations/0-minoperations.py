#!/usr/bin/python3
"""
This module contains functions that calculate the minimum
number of operations needed to get n number of 'H'
"""
import math


def isPrime(n):
    """
    return true if number is prime and false if not
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def allPrimeCandidates(n):
    """
    get all the prime numbers between 2 and sqrt(n)
    """
    prime_candidates = list()

    for i in range(2, n):
        if isPrime(i):
            prime_candidates.append(i)
    return prime_candidates


def getPrimeFactorsOf(n):
    """
    Return the prime factors of a number n
    """
    if not isinstance(n, int) or n <= 1:
        return []

    factors = []

    prime_candidates = sorted(allPrimeCandidates(n))

    n_copy = n

    while n_copy > 1 and prime_candidates:
        current_prime = prime_candidates.pop(0)
        while n_copy % current_prime == 0:
            factors.append(current_prime)
            n_copy /= current_prime
    return factors


def minOperations(n):
    """
    n is the number of H we need to make the computation for

    After careful observation i noticed the solution to the problem
    is just a summation of the prime factors of the number n
    """
    prime_factors = getPrimeFactorsOf(n)
    if prime_factors:
        return sum(prime_factors)
