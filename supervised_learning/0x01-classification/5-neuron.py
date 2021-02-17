#!/usr/bin/env python3
"""Neuron Gradient Descent"""
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
        """ Calculates the forward
        propagation of the neuron """
        Z = np.dot(self.__W, X) + self.__b
        self.__A = sigmoid(Z)
        return self.__A

    def cost(self, Y, A):
        """Calculates the cost of the
        model using logistic regression"""
        C = -np.sum((Y * np.log(A)) +
                    ((1 - Y) * np.log(1.0000001 - A))) / Y.shape[1]
        return C

    def evaluate(self, X, Y):
        """Evaluates the neuron’s predictions"""
        self.forward_prop(X)
        P = np.where(self.__A >= 0.5, 1, 0)
        C = self.cost(Y, self.__A)
        return P, C

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """Calculates one pass of
        gradient descent on the neuron"""
        n = Y.shape[1]
        dz = A - Y
        dw = np.dot(X, dz.T) / n
        db = np.sum(dz) / n
        self.__W = self.__W - (alpha * dw).T
        self.__b = self.__b - (alpha * db)


def sigmoid(z):
    """Sigmoid Activation function"""
    return 1.0 / (1.0 + np.exp(-z))
