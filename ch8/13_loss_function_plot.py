import os

import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([51.5, 55.1, 63.0, 71.2, 73.0, 77.1, 88.1, 91.2, 93.0, 101.6])
y = np.array([100.98, 137.44, 237.8, 254.96, 263.45, 353.89, 450.32, 521.34, 503.13, 573.91])

# Define the sum of squares loss function for a linear model: y = mx + b
def sum_of_squares_loss(m, b, x, y):
    y_pred = m * x + b
    return np.sum((y_pred - y) ** 2)

# Create meshgrid for m and b
m_range = np.linspace(-10, 10, 100)
b_range = np.linspace(-500, 500, 100)
M, B = np.meshgrid(m_range, b_range)
Z = np.zeros_like(M)

# Compute loss for each combination of m and b
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        Z[i, j] = sum_of_squares_loss(M[i, j], B[i, j], x, y)

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot surface
surface = ax.plot_surface(M, B, Z, cmap='viridis')

# Add labels and title
ax.set_xlabel('Slope (m)')
ax.set_ylabel('Intercept (b)')
ax.set_zlabel('Sum of Squares Loss')
ax.set_title('3D Plot of Sum of Squares Loss Function')

plt.tight_layout()
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)
# Show plot
plt.show()