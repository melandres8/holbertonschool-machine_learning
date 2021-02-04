#!/usr/bin/env python3
"""Initialize binomial"""


class Binomial:
    """represents a binomial distribution"""
    def __init__(self, data=None, n=1, p=0.5):
        """Constructor method"""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not 0 < p < 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) <= 2:
                raise ValueError("data must contain multiple values")
            mean = float(sum(data) / len(data))
            summa = [pow((x - mean), 2) for x in data]
            var = sum(summa) / len(data)
            p = 1 - var / mean
            if ((mean / p) - (mean // p)) >= 0.5:
                self.n = 1 + int(mean / p)
            else:
                self.n = int(mean / p)
            self.p = float(mean / self.n)

    def pmf(self, k):
        """
        Calculates the value of the PMF
        for a given number of "successes"
        """
        k = int(k)
        if k < 0:
            return 0

        factn = factk = factnk = 1
        for x in range(1, self.n + 1):
            factn *= x
        for x in range(1, k + 1):
            factk *= x
        for x in range(1, self.n - k + 1):
            factnk *= x

        return (factn / (factk * factnk)) * \
            self.p ** k * (1 - self.p) ** (self.n - k)
