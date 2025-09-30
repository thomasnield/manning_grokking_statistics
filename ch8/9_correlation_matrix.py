import pandas as pd

df = pd.DataFrame({
    'Sleep (hours)': [7.2,8.1,5.5,6.5,7.8],
    'Test Score': [85, 92, 78, 88, 95],
    'Attendance (%)': [95, 100, 80, 90, 98]
})
print(df)
correlations = df.corr(method='pearson')
print(correlations)

#                 Sleep (hours)  Test Score  Attendance (%)
# Sleep (hours)        1.000000    0.886531        0.990328
# Test Score           0.886531    1.000000        0.885657
# Attendance (%)       0.990328    0.885657        1.000000
