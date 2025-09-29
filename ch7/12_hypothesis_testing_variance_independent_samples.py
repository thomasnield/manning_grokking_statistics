from scipy.stats import f  #A

LEFT_TAIL, RIGHT_TAIL, TWO_TAIL = 0, 1, 2  #B

# MODIFY PARAMETERS IN THIS BOX  #C
# ==============================  #C
n_1 = 57  #C
n_2 = 35  #C
s_1 = .16  #C
s_2 = .21  #C
alpha = 0.05  #C
tail_type = TWO_TAIL  #C
# ==============================  #C

df_num = n_1 - 1  #D
df_den = n_2 - 1  #D

f_stat = s_1**2 / s_2**2  #E

if tail_type == TWO_TAIL:  #F
   print("TWO-TAIL TEST")  #F
   crit_val_left = f.ppf(alpha / 2, df_num, df_den)  #F
   crit_val_right = f.ppf(1 - (alpha / 2), df_num, df_den)  #F
   reject_h0 = f_stat < crit_val_left or f_stat > crit_val_right  #F
   print(f"Critical values: ({crit_val_left:.4f}, {crit_val_right:.4f})")  #F

elif tail_type == LEFT_TAIL:  #F
   print("LEFT TAIL TEST")  #F
   crit_val_left = f.ppf(alpha, df_num, df_den)  #F
   reject_h0 = f_stat < crit_val_left  #F
   print(f"Critical value: {crit_val_left:.4f}")  #F

elif tail_type == RIGHT_TAIL:  #F
   print("RIGHT TAIL TEST")  #F
   crit_val_right = f.ppf(1 - alpha, df_num, df_den)  #F
   reject_h0 = f_stat > crit_val_right  #F
   print(f"Critical value: {crit_val_right:.4f}")  #F

else:  #F
    raise ValueError("Invalid tail type. Choose from LEFT_TAIL, RIGHT_TAIL, or TWO_TAIL.")  #F

print(f"Alpha: {alpha}")  #G
print(f"Test statistic: {f_stat:.4f}")  #G

if reject_h0:  #H
    print("Reject the null hypothesis")  #H
else:  #H
    print("Fail to reject the null hypothesis")  #H

# TWO-TAIL TEST
# Critical values: (0.5553, 1.8855)
# Alpha: 0.05
# Test statistic: 0.5805
# Fail to reject the null hypothesis


#A Import the F-distribution from SciPy
#B Define constants for left-tailed, right-tailed, and two-tailed
#C Block for modifiable parameters
#D Compute degrees of freedom for numerator and denominator
#E Compute the F-test statistic as the ratio of the sample variances
#F Check the tail type, perform test
#G Print the alpha level and the computed test statistic
#H Print whether to reject the null hypothesis
