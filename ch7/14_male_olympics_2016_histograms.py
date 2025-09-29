import os

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
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

# Create three histograms
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].hist(group_a, bins=20, alpha=0.7)
axs[0].set_title('Swimming Male Weights')
axs[0].set_xlabel('Weight')
axs[0].set_ylabel('Frequency')

axs[1].hist(group_b, bins=20, alpha=0.7)
axs[1].set_title('Hockey Male Weights')
axs[1].set_xlabel('Weight')
axs[1].set_ylabel('Frequency')

axs[2].hist(group_c, bins=20, alpha=0.7)
axs[2].set_title('Tennis Male Weights')
axs[2].set_xlabel('Weight')
axs[2].set_ylabel('Frequency')

plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.tight_layout()
plt.show()