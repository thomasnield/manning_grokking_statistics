from scipy.stats import chi2

sigma = 200
n = 40
s = 285.84
alpha = .10

# Chi-Square Test Statistic
test_stat = (n - 1) * (s ** 2) / (sigma ** 2)

# Critical value for right-tailed test
crit_value = chi2.ppf(1 - alpha, n - 1)

# p-value
p_value = 1 - chi2.cdf(test_stat, n - 1)

# Output
print(f"Test Statistic: {test_stat:.4f}")
print(f"Critical Value: {crit_value:.2f}")
print(f"Alpha: {alpha}")
print(f"p-value: {p_value:.4f}")

if p_value < alpha: # can also quality with `test_stat > crit_value`
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

# Test Statistic: 79.6619
# Critical Value: 50.66
# Alpha: 0.1
# p-value: 0.0001
# Reject the null hypothesis