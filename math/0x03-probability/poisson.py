#!/usr/bin/env python3
"""Initialize Poisson"""


class Poisson:
    """Represents a poisson distribution"""
    def __init__(self, data=None, lambtha=1.):
        """Constructor method"""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Probability mass function.
        Calculates the value of the PMF for
        a given number of “successes”
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        result = 0
        factorial = 1

        for x in range(1, k + 1):
            factorial *= x

        result = ((2.7182818285 ** (-self.lambtha)) *
                  (self.lambtha ** k)) / factorial
        return result

    def cdf(self, k):
        """Cumulative Distribution Function.
            Calculates the value of the CDF for
            a given number of “successes”
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        result = 0
        suma = 0

        for i in range(k + 1):
            factorial = 1
            for x in range(1, i + 1):
                factorial *= x
            suma += (self.lambtha ** i) / factorial

        result = (2.7182818285 ** (-self.lambtha)) * suma
        return result
