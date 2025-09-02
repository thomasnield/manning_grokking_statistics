import os

import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt

n = 31 # sample size
alpha = .05
X = np.linspace(0,100,1000)
Y = chi2.pdf(X, df=n-1)

# PDF plot
plt.title(f"Chi-Square Distribution (df={n-1}, alpha={alpha})")
plt.xlabel("Chi-Square")
plt.ylabel("Probability Density")
plt.grid(True, alpha=0.3)
plt.plot(X, Y)

# Alpha plot
left_boundary, right_boundary = chi2.ppf(alpha/2, df=n-1), chi2.ppf(1-alpha/2, df=n-1)
shade_x = X[(X <= left_boundary)]
shade_y = chi2.pdf(shade_x, n-1)
plt.fill_between(shade_x, shade_y, color="blue")

shade_x = X[(X >= right_boundary)]
shade_y = chi2.pdf(shade_x, n-1)
plt.fill_between(shade_x, shade_y, color="blue")

plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()