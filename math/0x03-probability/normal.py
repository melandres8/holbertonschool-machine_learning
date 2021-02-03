#!/usr/bin/env python3
"""Initialize normal"""


class Normal:
    """represents a normal distribution"""
    def __init__(self, data=None, mean=0., stddev=1.):
        """Constructor"""
        if data is None:
            if stddev < 0:
                raise ValueError("stddev must be a positive value")
            self.stddev = float(stddev)
            self.mean = float(mean)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            summa = [(x - self.mean) ** 2 for x in data]
            self.stddev = pow((sum(summa) / len(data)), .5)
