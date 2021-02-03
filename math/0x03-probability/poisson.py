#!/usr/bin/env python3
"""Initialize Poisson"""


class Poisson:
    """Represents a poisson distribution"""
    def __init__(self, data=None, lambtha=1.):
        """Constructor method"""
        if data is None:
            self.lambtha = float(lambtha)
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        else:
            self.lambtha = float(sum(data) / len(data))
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
