#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

names = ['Farrah', 'Fred', 'Felicia']
fruits = {
    'apples': 'red',
    'bananas': 'yellow',
    'oranges': '#ff8000',
    'peaches': '#ffe5b4'
    }

offset = [0, 0, 0]

for k, v in fruits.items():
    for row in range(len(fruit)):
        plt.bar(
            np.arange(len(names)),
            fruit[row],
            0.5,
            bottom=offset,
            color=v,
            label=k
        )
        offset += fruit[row]

plt.title('Number of Fruit per Person')
plt.ylabel('Quantity of Fruit')
plt.yticks(np.arange(0, 90, step=10))
plt.xticks(np.arange(len(names)), names)

plt.legend(loc='upper right')
plt.show()
