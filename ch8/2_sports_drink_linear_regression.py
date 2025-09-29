import os

from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

x = np.array([ 51.5,  55.1,  63.0,  71.2,  73.0 , 77.1,  88.1,  91.2,  93.0, 101.6])
y = np.array([100.98, 137.44, 237.8 , 254.96, 263.45, 353.89, 450.32, 521.34, 503.13, 573.91])

r, p = pearsonr(x, y)
print(f"Pearson correlation: {r:.4f}")

# Create the scatter plot
plt.scatter(x, y)
slope, intercept, r_value, p_value, std_err = linregress(x, y)
line_of_best_fit = slope * x + intercept
print(f"Slope: {slope:.4f}, Intercept: {intercept:.4f}")

plt.plot(x, line_of_best_fit, color='red', label='Line of Best Fit')

# Add title and labels
plt.title("Temperature vs Sports Drink Sales")
plt.xlabel("Temperature (Fahrenheit)")
plt.ylabel("Sports Drink Sales")

plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)
# Display the plot
plt.show()