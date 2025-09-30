import numpy as np
from scipy.stats import linregress

x = np.array([51.5, 55.1, 63.0, 71.2, 73.0, 77.1, 88.1, 91.2, 93.0, 101.6])
y = np.array([100.98, 137.44, 237.8, 254.96, 263.45, 353.89, 450.32, 521.34, 503.13, 573.91])

# Perform linear regression using SciPy
m, b, r_value, p_value, std_err = linregress(x, y)

# Print the regression results
print(f"Slope: {m:.2f} (sales increase per degree Fahrenheit)")
print(f"Intercept: {b:.2f}")
print(f"Pearson Correlation: {r_value:.4f}")
print(f"P-value (for slope): {p_value:.10f}")
print(f"Standard error of slope: {std_err:.4f}")

# Slope: 9.74 (sales increase per degree Fahrenheit)
# Intercept: -405.26
# Pearson Correlation: 0.9889
# P-value (for slope): 0.0000000654
# Standard error of slope: 0.5173