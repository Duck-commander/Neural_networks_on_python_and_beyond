import numpy as np


def sigmoid(x):
    # Функция активации: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))


class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
    
    def feedforward(self, inputs):
        # Прямое распространение
        # Вводные данные о весе, добавление смещения 
        # и последующее использование функции активации
        total = np.dot(self.weights, inputs) + self.bias 
        return sigmoid(total)


weights = np.array([0, 1])
bias = 0
n = Neuron(weights, bias)

x = np.array([2, 3])
print(n.feedforward(x))