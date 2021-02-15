#!/usr/bin/env python3
"""Neuron Forward Propagation"""
import numpy as np


class Neuron:
    """Defines a single neuron performing
    binary classification"""
    def __init__(self, nx):
        """Constructor

        Args:
            nx (int): is the number of input features to the neuron.

        Raises:
            TypeError: nx must be an integer
            ValueError: nx must be a positive integer
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """The weights vector for the neuron. """
        return self.__W

    @property
    def b(self):
        """The bias for the neuron."""
        return self.__b

    @property
    def A(self):
        """The activated output of
        the neuron (prediction)."""
        return self.__A

    def forward_prop(self, X):
        """ defines a single neuron
        performing binary classification """
        Z = np.dot(self.__W, X) + self.__b
        self.__A = sigmoid(Z)
        return self.__A


def sigmoid(z):
    """Sigmoid Activation function"""
    return 1.0 / (1.0 + np.exp(-z))
