from scipy.stats import chi2

n = 31
alpha = .05

left_boundary = chi2.ppf(alpha/2, df=n-1)
right_boundary = chi2.ppf(1 - alpha/2, df=n-1)

# Left tail boundary: 16.7908
print(f"Left tail boundary: {left_boundary:.4f}")

# Right tail boundary: 46.9792
print(f"Right tail boundary: {right_boundary:.4f}")
