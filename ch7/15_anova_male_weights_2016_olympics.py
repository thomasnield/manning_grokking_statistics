import pandas as pd
import numpy as np
from scipy.stats import f_oneway

# Load the CSV file
df = pd.read_csv("athlete_events.csv")

# Filter for Year=2016, Sex='M', and Weight not null
df = df[(df['Year'] == 2016) &
                 (df['Sex'] == 'M') &
                 df['Weight'].notna()]

# Group by SPORT and NAME, compute MAX(Weight) as WEIGHT
# to remove duplicates of athletes competing in multiple vents
df = df.groupby(['Sport', 'Name'])['Weight'].max().reset_index()

# Perform ANOVA
group_a = df[df['Sport'] == 'Swimming']['Weight']
group_b = df[df['Sport'] == 'Hockey']['Weight']
group_c = df[df['Sport'] == 'Tennis']['Weight']

print(f"A: x̄ = {np.mean(group_a):.4f}, s = {np.std(group_a,ddof=1):.4f}")
print(f"B: x̄ = {np.mean(group_b):.4f}, s = {np.std(group_b,ddof=1):.4f}")
print(f"C: x̄ = {np.mean(group_c):.4f}, s = {np.std(group_c,ddof=1):.4f}")

f_statistic, p_value = f_oneway(group_a, group_b, group_c)

# Print the results
print(f"f_statistic: {f_statistic:.4f}, p_value: {p_value:.4f}")
# A: x̄ = 79.7906, s = 8.6463
# B: x̄ = 77.2755, s = 6.9670
# C: x̄ = 79.8857, s = 7.2102
# f_statistic: 7.2418, p_value: 0.0008