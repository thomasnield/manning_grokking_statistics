from scipy.stats import chi2

sigma = 200 # Population standard deviation
n = 40 # Sample size
s = 285.84 # Sample standard deviation
alpha = .05 # Significance level

test_stat = (n - 1) * (s ** 2) / (sigma ** 2) # # Chi-Square Test Statistic

crit_value = chi2.ppf(1 - alpha, n - 1) # Critical value for right-tailed test

p_value = 1 - chi2.cdf(test_stat, n - 1) # Calculate the p-value

print(f"Test Statistic: {test_stat:.4f}") # Test Statistic: 79.6619
print(f"Critical Value: {crit_value:.2f}") # Critical Value: 50.66
print(f"Alpha: {alpha}") # Alpha: .05
print(f"p-value: {p_value:.4f}") # p-value: 0.0001

if p_value < alpha: # can also quality with `test_stat > crit_value`
    print("Reject the null hypothesis") # Reject the null hypothesis
else:
    print("Fail to reject the null hypothesis")