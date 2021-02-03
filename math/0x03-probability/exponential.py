#!/usr/bin/env python3
"""Initialize Exponential"""


class Exponential:
    """represents an exponential distribution"""
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
            self.lambtha = 1 / float(sum(data) / len(data))

    def pdf(self, x):
        """
        Calculates the value of the PDF
        for a given time period
        """
        if x < 0:
            result = 0
        else:
            result = self.lambtha * 2.7182818285 ** (-self.lambtha * x)

        return result

    def cdf(self, x):
        """
        Calculates the value of the CDF
        for a given time period
        """
        if x < 0:
            result = 0
        else:
            result = 1 - 2.7182818285 ** (-self.lambtha * x)

        return result
