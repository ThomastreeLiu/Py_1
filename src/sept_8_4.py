import matplotlib.pyplot as plt
import numpy as np

theta = np.arange(0, 361)
cost = np.cos(np.radians(theta))
sint = np.cos(np.radians(theta))

plt.subplot(1, 2, 1)
plt.plot(theta, cost)
plt.show()
