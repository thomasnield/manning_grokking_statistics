import os

import matplotlib.pyplot as plt
import numpy as np

x = np.array([ 51.5,  55.1,  63.0,  71.2,  73.0 , 77.1,  88.1,  91.2,  93.0, 101.6])
y = np.array([100.98, 137.44, 237.8 , 254.96, 263.45, 353.89, 450.32, 521.34, 503.13, 573.91])

# Create the scatter plot
plt.scatter(x, y)

# Add title and labels
plt.title("Temperature vs Sports Drink Sales")
plt.xlabel("Temperature (Fahrenheit)")
plt.ylabel("Sports Drink Sales")

plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)
# Display the plot
plt.show()