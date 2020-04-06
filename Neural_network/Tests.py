import matplotlib.pyplot as plt
import numpy as np
from Just_neuron import sigmoid


fig, ax = plt.subplots()

x = np.linspace(-5, 5, 100)
y = sigmoid(x)

ax.plot(x, y)

plt.show()