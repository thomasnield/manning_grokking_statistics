import numpy as np
from scipy.stats import f

k = 3  #A

X_1 = np.array([84, 80, 84, 90, 79, 79, 90, 85,
                77, 84, 77, 77, 82, 68, 70])  #B

X_2 = np.array([68, 64, 76, 65, 60, 86, 71, 73,
                60, 68, 74, 62, 76, 67, 70, 67,
                90, 73, 63, 80])  #C

X_3 = np.array([71, 82, 65, 70, 82, 86, 82, 80,
                78, 69, 75, 77])  #D

all_data = np.concatenate([X_1, X_2, X_3])  #E
N = len(all_data)  #E
grand_mean = np.mean(all_data)  #E

SST = np.sum((all_data - grand_mean)**2)  #F

group_means = [np.mean(group) for group in [X_1, X_2, X_3]] #G
group_sizes = [len(group) for group in [X_1, X_2, X_3]]  #G
SSB = np.sum([size * (mean - grand_mean)**2 for size, mean in zip(group_sizes, group_means)])  #G

SSW = SST - SSB  #H

df_between = k - 1  #I
df_within = N - k  #I

MSB = SSB / df_between  #J
MSW = SSW / df_within  #J

F_stat = MSB / MSW  #K

p_value = 1 - f.cdf(F_stat, df_between, df_within)  #L

print(f"Grand mean: {grand_mean}")
print(f"SST: {SST}")
print(f"SSB: {SSB}")
print(f"SSW: {SSW}")
print(f"DF between: {df_between}, DF within: {df_within}")
print(f"MSB: {MSB}")
print(f"MSW: {MSW}")
print(f"F-statistic: {F_stat:.4f}")
print(f"p-value: {p_value:.4f}")  #M

#A number of groups
#B observations for group 1
#C observations for group 2
#D observations for group 3
#E Combine all data for grand mean calculation
#F Total sum of squares (SST)
#G Between-group sum of squares (SSB)
#H Within-group sum of squares (SSW = SST - SSB)
#I Degrees of freedom
#J Mean squares
#K F-statistic
#L p-value using F-distribution CDF
#M Output results
