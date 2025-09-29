import numpy as np  #A
from scipy.stats import f_oneway, f  #B

X_1 = np.array([84, 80, 84, 90, 79, 79, 90, 85,
                77, 84, 77, 77, 82, 68, 70])  #C

X_2 = np.array([68, 64, 76, 65, 60, 86, 71, 73,
                60, 68, 74, 62, 76, 67, 70, 67,
                90, 73, 63, 80])  #D

X_3 = np.array([71, 82, 65, 70, 82, 86, 82, 80,
                78, 69, 75, 77])  #E

f_stat, p_value = f_oneway(X_1, X_2, X_3)  #F

print(f"f_stat: {f_stat:.4f}")  #G
print(f"p_value: {p_value:.4f}")  #G

# f_stat: 8.1474, p_value: 0.0010  #H

#A Import NumPy for array operations
#B Import one-way ANOVA function and F distribution from SciPy
#C Define the first sample data array
#D Define the second sample data array
#E Define the third sample data array
#F Compute the F-statistic and p-value using one-way ANOVA
