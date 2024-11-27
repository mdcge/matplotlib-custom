import matplotlib.pyplot as plt
import numpy as np

plt.style.use('maxplotlib.mplstyle')

# Data
rng = np.random.default_rng(seed=0)

wave_xs = np.linspace(0, 10, 1000)
wave_ys1 = 2*np.sin(5*wave_xs+3) + 0.2*np.cos(13*wave_xs-1) + 8*np.sin(1.3*wave_xs+5) + 0.4*np.sin(52*wave_xs+3)
wave_ys2 = 3*np.sin(7*wave_xs+14) + 0.3*np.cos(11*wave_xs) + 6*np.sin(1.7*wave_xs+1) + 0.3*np.cos(63*wave_xs-9)
point_xs = np.linspace(0, 10, 20)
point_ys = 5*np.sin(0.9*point_xs+22) + rng.normal(scale=1.5, size=len(point_xs))

# Plot
plt.plot(wave_xs, wave_ys1, zorder=2, label="run 1")
plt.plot(wave_xs, wave_ys2, zorder=2, label="run 2")
plt.plot([min(wave_xs), max(wave_xs)], [0.5*max(wave_ys1)]*2, linestyle='dashed', zorder=1, label="cutoff")
plt.plot(point_xs, point_ys, 'o-', label="theory")
plt.grid()

# Decorate
plt.title("This is a plot")
plt.xlabel("Some parameter (unit)")
plt.ylabel("Some other parameter (other unit)")
plt.legend()
plt.savefig("example-plot.pdf", bbox_inches='tight')
plt.show()
