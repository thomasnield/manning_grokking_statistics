import os

import numpy as np  #A
import matplotlib.pyplot as plt  #A
from scipy.stats import pearsonr  #A

def generate_correlated_data(n, corr):  #B
    mean = [0, 0]  #B
    cov = [[1, corr], [corr, 1]]  #B
    data = np.random.multivariate_normal(mean, cov, n)  #B
    return data[:, 0], data[:, 1]  #B

n_points = 100  #C
correlations = [-0.9, -0.5, 0.0, 0.5, 0.9]  #D
titles = ['Strong Negative', 'Moderate Negative', 'Zero', 'Moderate Positive', 'Strong Positive']  #E

fig, axs = plt.subplots(1, 5, figsize=(20, 4))  #F

for i, (corr, title) in enumerate(zip(correlations, titles)):  #G
    x, y = generate_correlated_data(n_points, corr)  #G
    r, _ = pearsonr(x, y)  #G
    axs[i].scatter(x, y, alpha=0.6)  #G
    axs[i].set_title(f'{title}\n(r ≈ {r:.2f})')  #G
    axs[i].set_xlabel('X')  #G
    axs[i].set_ylabel('Y')  #G

plt.tight_layout()  #H

plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()  #H


#A Import necessary libraries for data generation, plotting, and correlation calculation
#B Define a function to generate correlated data using multivariate normal distribution
#C Set the number of points for each scatterplot
#D Define the target correlation values for each panel
#E Define descriptive titles for each correlation level
#F Create a figure with 5 subplots arranged in a row
#G Loop through each correlation: generate data, compute actual Pearson r, create scatterplot, and set title/labels
#H Adjust layout and display the plot