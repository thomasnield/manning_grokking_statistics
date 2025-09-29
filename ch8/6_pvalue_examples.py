import os

import numpy as np  #A
import matplotlib.pyplot as plt  #A
from scipy.stats import pearsonr  #A

def generate_correlated_data(n, corr):  #B
    mean = [0, 0]  #B
    cov = [[1, corr], [corr, 1]]  #B
    data = np.random.multivariate_normal(mean, cov, n)  #B
    return data[:, 0], data[:, 1]  #B

corrs = [0.99, 0.99, 0.9, 0.2]  #C
n_points = [2, 3, 10, 20]  #D
titles = [f'n={n}' for n in n_points]  #E

fig, axs = plt.subplots(1, 4, figsize=(20, 4))  #F

for i, (n, title) in enumerate(zip(n_points, titles)):  #G
    x, y = generate_correlated_data(n, corrs[i])  #G
    r, p = pearsonr(x, y)  #G
    axs[i].scatter(x, y, alpha=0.6)  #G
    axs[i].set_title(f'{title}\n(r ≈ {r:.2f}, p ≈ {p:.8f})')  #G
    axs[i].set_xlabel('X')  #G
    axs[i].set_ylabel('Y')  #G

plt.tight_layout()  #H
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)
plt.show()  #H

#A Import necessary libraries for data generation, plotting, and correlation calculation
#B Define a function to generate correlated data using multivariate normal distribution
#C Set the fixed high correlation value for all panels
#D Define the sample sizes for each panel
#E Generate titles based on sample sizes
#F Create a figure with 5 subplots arranged in a row
#G Loop through each sample size: generate data, compute Pearson r and p-value, create scatterplot, and set title/labels
#H Adjust layout and display the plot