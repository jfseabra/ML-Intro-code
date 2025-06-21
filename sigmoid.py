import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.sans-serif": ["Computer Modern Sans Serif"],
    "figure.dpi": 300})

x = np.linspace(-10, 10, 1001)
plt.plot(x, 1.0 / (1.0 + np.exp(-x)))
plt.xlim((-10.5, 10.5))
plt.xlabel(r'$x$')
plt.ylabel(r'$\sigma(x)$')
plt.savefig('Plots/Sigmoid.png')
#plt.show()
