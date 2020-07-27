import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = x + np.random.randn(100) 

plt.plot(x, y, label="test")

plt.legend()

plt.show()