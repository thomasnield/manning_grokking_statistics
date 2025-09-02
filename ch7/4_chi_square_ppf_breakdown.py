import os

import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt

n = 31 # sample size
alpha = .05
df = n - 1
X = np.linspace(0,100,1000)
Y = chi2.pdf(X, df=df)

left_boundary = chi2.ppf(alpha/2, df=df)
right_boundary = chi2.ppf(1-alpha/2, df=df)

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Left panel: Lower tail
axs[0].plot(X, Y)
axs[0].set_title(f"Lower Tail: α/2 = {alpha/2}")
axs[0].set_xlabel("Chi-Square")
axs[0].set_ylabel("Probability Density")
axs[0].grid(True, alpha=0.3)
shade_idx = X <= left_boundary
axs[0].fill_between(X[shade_idx], Y[shade_idx], color="blue")
axs[0].axvline(left_boundary, color='red', linestyle='--')

# Right panel: Upper tail
axs[1].plot(X, Y)
axs[1].set_title(f"Upper Tail: 1 - α/2 = {1 - alpha/2}")
axs[1].set_xlabel("Chi-Square")
axs[1].set_ylabel("Probability Density")
axs[1].grid(True, alpha=0.3)
shade_idx = X <= right_boundary
axs[1].fill_between(X[shade_idx], Y[shade_idx], color="blue")
axs[1].axvline(right_boundary, color='red', linestyle='--')

fig.suptitle(f"Chi-Square Distribution (df={df}, alpha={alpha})")
plt.tight_layout()

plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()