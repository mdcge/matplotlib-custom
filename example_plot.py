import matplotlib.pyplot as plt
import numpy as np

# Data
xs = np.linspace(0, 10, 1000)
ys1 = 2*np.sin(5*xs+3) + 0.2*np.cos(13*xs-1) + 8*np.sin(1.3*xs+5) + 0.4*np.sin(52*xs+3)
ys2 = 3*np.sin(7*xs+14) + 0.3*np.cos(11*xs) + 6*np.sin(1.7*xs+1) + 0.3*np.cos(63*xs-9)

# Plot
plt.plot(xs, ys1, zorder=2, label="run 1")
plt.plot(xs, ys2, zorder=2, label="run 2")
plt.plot([min(xs), max(xs)], [0.5*max(ys1)]*2, linestyle='dashed', zorder=1, label="cutoff")
plt.grid()

# Decorate
plt.title("This is a plot")
plt.xlabel("Some parameter (unit)")
plt.ylabel("Some other parameter (other unit)")
plt.legend()
plt.savefig("example-plot.pdf", bbox_inches='tight')
plt.show()
