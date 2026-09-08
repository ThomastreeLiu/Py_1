import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11)
y = np.random.randint(1, 7, 10)
plt.plot(x, y)
plt.axis([0, 10, 0, 10])
plt.show()
plt.bar(x, y)
plt.show()
