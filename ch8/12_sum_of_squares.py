import numpy as np

x = np.array([51.5, 55.1, 63.0, 71.2, 73.0, 77.1, 88.1, 91.2, 93.0, 101.6])
y = np.array([100.98, 137.44, 237.8, 254.96, 263.45, 353.89, 450.32, 521.34, 503.13, 573.91])

# we are calculating the sum of squares for a line
# with these coefficients
m = 9.74
b = -405.26

sum_of_squares = 0
for i in range(len(x)):
    actual_y = y[i]
    predicted_y = m * x[i] + b
    sum_of_squares += (actual_y - predicted_y) ** 2

print(f"Sum of squares: {sum_of_squares:.2f}")
# Sum of squares: 5477.72