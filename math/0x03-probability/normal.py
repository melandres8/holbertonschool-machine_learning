#!/usr/bin/env python3
"""Initialize normal"""


class Normal:
    """represents a normal distribution"""
    def __init__(self, data=None, mean=0., stddev=1.):
        """Constructor"""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.stddev = float(stddev)
            self.mean = float(mean)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) <= 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            summa = [(x - self.mean) ** 2 for x in data]
            self.stddev = pow((sum(summa) / len(data)), 0.5)

    def z_score(self, x):
        """Calculates the z-score
        of a given x-value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value
        of a given z-score"""
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Calculates the value of the
        PDF for a given x-value"""
        return 1 / (self.stddev * (2 * 3.1415926536) ** 0.5) * \
            2.7182818285 ** (-(x - self.mean) ** 2 / (2 * self.stddev ** 2))
