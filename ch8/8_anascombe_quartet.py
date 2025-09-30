import os

import matplotlib.pyplot as plt
import numpy as np

# Anscombe's Quartet datasets
x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])
y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])
y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89])

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Anscombe's Quartet")

# Plot dataset I
axs[0, 0].scatter(x, y1)
axs[0, 0].plot([3, 20], [4.5, 13], 'r')  # Regression line: y = 3 + 0.5x
axs[0, 0].set_title('I')
axs[0, 0].set_xlim(2, 20)
axs[0, 0].set_ylim(2, 14)

# Plot dataset II
axs[0, 1].scatter(x, y2)
axs[0, 1].plot([3, 20], [4.5, 13], 'r')
axs[0, 1].set_title('II')
axs[0, 1].set_xlim(2, 20)
axs[0, 1].set_ylim(2, 14)

# Plot dataset III
axs[1, 0].scatter(x, y3)
axs[1, 0].plot([3, 20], [4.5, 13], 'r')
axs[1, 0].set_title('III')
axs[1, 0].set_xlim(2, 20)
axs[1, 0].set_ylim(2, 14)

# Plot dataset IV
axs[1, 1].scatter(x4, y4)
axs[1, 1].plot([3, 20], [4.5, 13], 'r')
axs[1, 1].set_title('IV')
axs[1, 1].set_xlim(2, 20)
axs[1, 1].set_ylim(2, 14)

# Adjust layout and show the plot
plt.tight_layout()
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)
plt.show()
