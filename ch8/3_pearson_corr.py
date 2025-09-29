from scipy.stats import pearsonr
import numpy as np

x = np.array([ 51.5,  55.1,  63.0,  71.2,  73.0 , 77.1,  88.1,  91.2,  93.0, 101.6])
y = np.array([100.98, 137.44, 237.8 , 254.96, 263.45, 353.89, 450.32, 521.34, 503.13, 573.91])


r = (sum((x - np.mean(x)) * (y - np.mean(y))) /
     np.sqrt(sum((x-np.mean(x))**2) * sum((y - np.mean(y))**2)))

print(f"Pearson correlation (manual): {r:.4f}")

r, p = pearsonr(x, y)
print(f"Pearson correlation (SciPy): {r:.4f}, p-value: {p:.10f}")
# Pearson correlation (manual): 0.9889
# Pearson correlation (SciPy): 0.9889, p-value: 0.0000000654