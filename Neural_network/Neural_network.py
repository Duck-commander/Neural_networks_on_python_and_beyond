import numpy as np
from Just_neuron import sigmoid, Neuron


class FirstNeuralNetwork:
    """
    Нейронная сеть, у которой: 
        - 2 входа
        - 1 скрытый слой с двумя нейронами (h1, h2) 
        - слой вывода с одним нейроном (o1)
    У каждого нейрона одинаковые вес и смещение:
        - w = [0, 1]
        - b = 0
    """

    def __init__(self):
        weights = np.array([0, 1])
        bias = 0

        self.h1 = Neuron(weights, bias)
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)

    def feedforward(self, x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)

        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))

        return out_o1


network = FirstNeuralNetwork()
x = np.array([2, 3])
print(network.feedforward(x))