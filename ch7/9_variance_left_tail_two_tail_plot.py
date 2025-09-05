import os

import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt

n = 31 # sample size
alpha = .05
df = n - 1
X = np.linspace(0,100,1000)
Y = chi2.pdf(X, df=df)

# For one-tailed (right-tailed)
one_tailed_critical = chi2.ppf(alpha, df=df)

# For two-tailed
two_tailed_left_critical = chi2.ppf(alpha / 2, df=df)
two_tailed_right_critical = chi2.ppf(1 - alpha / 2, df=df)

print(f"One-tailed critical value: {one_tailed_critical:.4f}")
print(f"Two-tailed left critical value: {two_tailed_left_critical:.4f}")
print(f"Two-tailed right critical value: {two_tailed_right_critical:.4f}")

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Left panel: One-tailed test (left-tailed)
axs[0].plot(X, Y)
axs[0].set_title(f"Left-Tailed Test: α = {alpha}")
axs[0].set_xlabel("Chi-Square")
axs[0].set_ylabel("Probability Density")
axs[0].grid(True, alpha=0.3)
shade_idx = X <= one_tailed_critical
axs[0].fill_between(X[shade_idx], Y[shade_idx], color="blue")
axs[0].axvline(one_tailed_critical, color='red', linestyle='--')

# Right panel: Two-tailed test
axs[1].plot(X, Y)
axs[1].set_title(f"Two-Tailed Test: α = {alpha}")
axs[1].set_xlabel("Chi-Square")
axs[1].set_ylabel("Probability Density")
axs[1].grid(True, alpha=0.3)
shade_left_idx = X <= two_tailed_left_critical
shade_right_idx = X >= two_tailed_right_critical
axs[1].fill_between(X[shade_left_idx], Y[shade_left_idx], color="blue")
axs[1].fill_between(X[shade_right_idx], Y[shade_right_idx], color="blue")
axs[1].axvline(two_tailed_left_critical, color='red', linestyle='--')
axs[1].axvline(two_tailed_right_critical, color='red', linestyle='--')

fig.suptitle(f"Chi-Square Distribution (df={df}, alpha={alpha})")
plt.tight_layout()

plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()