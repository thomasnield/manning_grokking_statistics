import os

import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt

n = 31 # sample size
X = np.linspace(0,100,1000)
Y = chi2.pdf(X, df=n-1)

plt.title(f"Chi-Square Distribution (df={n-1})")
plt.xlabel("Chi-Square")
plt.ylabel("Probability Density")
plt.grid(True, alpha=0.3)
plt.plot(X, Y)

plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()