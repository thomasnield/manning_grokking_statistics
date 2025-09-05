import os

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.linspace(0, 20, 1000)  #A

y1 = stats.chi2.pdf(x, 2)  #B

y2 = stats.chi2.pdf(x, 5)  #C

y3 = stats.chi2.pdf(x, 10)  #D

plt.figure(figsize=(8, 5))  #E
plt.grid(False)  #E
plt.plot(x, y1, color='black', linestyle='-', label='χ²(2)')  #E
plt.plot(x, y2, color='darkgray', linestyle='--', label='χ²(5)')  #E
plt.plot(x, y3, color='darkgray', linestyle=':', label='χ²(10)')  #E
plt.title('Comparison of Chi-Squared Distributions with Different Degrees of Freedom')  #E
plt.xlabel(r"$\chi^2$")  #E
plt.ylabel('Probability Density')  #E
plt.legend()  #E

plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)
plt.show()  #E

#A Define x range
#B Chi-squared distribution: df=2
#C Chi-squared distribution: df=5
#D Chi-squared distribution: df=10
#E Create the plot with grayscale colors and varied line styles