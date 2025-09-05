import os

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Chi-square distribution (degrees of freedom = 5)
df_chi = 5
x_chi = np.linspace(0, 20, 1000)
y_chi = stats.chi2.pdf(x_chi, df_chi)

# F-distribution (numerator df = 5, denominator df = 10)
dfn = 5
dfd = 10
x_f = np.linspace(0, 5, 1000)
y_f = stats.f.pdf(x_f, dfn, dfd)

# Create side-by-side plots
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].plot(x_chi, y_chi, label=r"$\chi^2$ pdf")
axs[0].set_title(r"$\chi^2$ Distribution ($dof$=" f"{df_chi})")
axs[0].set_xlabel(r"$\chi^2$")
axs[0].set_ylabel('Probability density')
axs[0].legend()
axs[0].grid(True)

axs[1].plot(x_f, y_f, label='F pdf')
axs[1].set_title(f'F Distribution ($dof_n$={dfn}, $dof_d$={dfd})')
axs[1].set_xlabel('F')
axs[1].set_ylabel('Probability density')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()