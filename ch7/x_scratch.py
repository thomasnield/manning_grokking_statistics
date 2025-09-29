from math import sqrt  #A
from scipy.stats import f

LEFT_TAIL, RIGHT_TAIL, TWO_TAIL = 0, 1, 2  #B

# MODIFY PARAMETERS IN THIS BOX
# ==============================
n_1 = 57
n_2 = 35
s_1 = .16
s_2 = .21
alpha = 0.05
tail_type = TWO_TAIL
# ==============================

# Degrees of freedom
df_num = n_1 - 1
df_den = n_2 - 1

# Test statistic
f_stat = s_1**2 / s_2**2

# check
if tail_type == TWO_TAIL:  #F
   print("TWO-TAIL TEST")  #F
   crit_val_left = f.ppf(alpha / 2, df_num, df_den)
   crit_val_right = f.ppf(1 - (alpha / 2), df_num, df_den)
   reject_h0 = f_stat < crit_val_left or f_stat > crit_val_right
   print(f"Critical values: ({crit_val_left:.4f}, {crit_val_right:.4f})")

elif tail_type == LEFT_TAIL:  #F
   print("LEFT TAIL TEST")  #F
   crit_val_left = f.ppf(alpha, df_num, df_den)
   reject_h0 = f_stat < crit_val_left
   print(f"Critical value: {crit_val_left:.4f}")

elif tail_type == RIGHT_TAIL:  #F
   print("RIGHT TAIL TEST")  #F
   crit_val_right = f.ppf(1 - alpha, df_num, df_den)
   reject_h0 = f_stat > crit_val_right
   print(f"Critical value: {crit_val_right:.4f}")

else:  #F
    raise ValueError("Invalid tail type. Choose from LEFT_TAIL, RIGHT_TAIL, or TWO_TAIL.")  #F

print(f"Alpha: {alpha}")
print(f"Test statistic: {f_stat:.4f}")

if reject_h0:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

# TTWO-TAIL TEST
# Critical values: (0.5553, 1.8855)
# Alpha: 0.05
# Test statistic: 0.5805
# Fail to reject the null hypothesis