import os

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Define x range
x = np.linspace(0, 10, 1000)

# F-distribution 1: dfn=2, dfd=2
y1 = stats.f.pdf(x, 2, 2)

# F-distribution 2: dfn=5, dfd=5
y2 = stats.f.pdf(x, 5, 5)

# F-distribution 3: dfn=10, dfd=30
y3 = stats.f.pdf(x, 10, 30)

# Create the plot with grayscale colors and varied line styles
plt.figure(figsize=(8, 5))
plt.grid(False)
plt.plot(x, y1, color='black', linestyle='-', label='F(2,2)')  # Solid black
plt.plot(x, y2, color='darkgray', linestyle='--', label='F(5,5)')  # Dashed dark gray
plt.plot(x, y3, color='darkgray', linestyle=':', label='F(10,30)')  # Dotted light gray
plt.title('Comparison of F-Distributions with Different Degrees of Freedom')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)
plt.show()