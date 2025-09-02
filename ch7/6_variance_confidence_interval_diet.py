from scipy.stats import chi2
from math import sqrt

# Given values
n = 40
s = 285.84
confidence_level = 0.90
alpha = 1 - confidence_level

chi2_crit_lower_tail = chi2.ppf(alpha / 2, n-1)
chi2_crit_upper_tail = chi2.ppf(1 - alpha / 2, n-1)

print(f"Chi-squared critical values: ({chi2_crit_lower_tail:.4f},{chi2_crit_upper_tail:.4f})") # Chi-squared critical values: (25.6954,54.5722)

# Confidence interval for variance
lower_bound = sqrt((n-1) * (s**2) / chi2_crit_upper_tail)
upper_bound = sqrt((n-1) * (s**2) / chi2_crit_lower_tail)

print(f"The {int(confidence_level * 100)}% confidence interval for the population standard deviation" ""
      f" is ({lower_bound:.4f}, {upper_bound:.4f})") # The 90% confidence interval for the population standard deviation is (241.6404, 352.1500)





