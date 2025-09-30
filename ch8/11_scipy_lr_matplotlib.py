import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

x = np.array([51.5, 55.1, 63.0, 71.2, 73.0, 77.1, 88.1, 91.2, 93.0, 101.6])  #A
y = np.array([100.98, 137.44, 237.8, 254.96, 263.45, 353.89, 450.32, 521.34, 503.13, 573.91])  #A

slope, intercept, r_value, p_value, std_err = linregress(x, y)  #B

x_line = np.linspace(min(x), max(x), 100)  #C
y_line = slope * x_line + intercept  #C

plt.scatter(x, y, label='Data points')  #D

plt.plot(x_line,  #E
         y_line,  #E
         color='red',  #E
         label=f'Fit: y = {slope:.2f}x {'-' if intercept < 0 else '+'} {abs(intercept):.2f}')  #E

plt.title("Temperature vs Sports Drink Sales")  #F
plt.xlabel("Temperature (Fahrenheit)")  #F
plt.ylabel("Sports Drink Sales")  #F
plt.legend()  #F

plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()  #G

print(f"Slope: {slope:.2f} (sales increase per degree Fahrenheit)")  #H
print(f"Intercept: {intercept:.2f}")  #H
print(f"Pearson Correlation: {r_value:.4f}")  #H
print(f"P-value (for slope): {p_value:.10f}")  #H
print(f"Standard error of slope: {std_err:.4f}")  #H

#A Temperature and sales data arrays
#B Perform linear regression using SciPy
#C Create the regression line
#D Create the scatter plot
#E Plot the regression line
#F Add title, labels, and legend
#G Display the plot
#H Print the regression results