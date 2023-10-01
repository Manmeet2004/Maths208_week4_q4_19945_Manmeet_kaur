import datetime
import numpy as np
from scipy import stats

# Data
data = [11, 14, 15, 15, 16, 16, 17, 18, 19, 21, 25, 36,
        12, 14, 15, 15, 16, 16, 17, 18, 19, 21, 25, 39,
        13, 14, 15, 15, 16, 17, 17, 18, 20, 22, 26, 43,
        13, 14, 15, 15, 16, 17, 17, 18, 20, 22, 26, 46,
        13, 14, 15, 16, 16, 17, 17, 18, 20, 22, 27, 50,
        13, 14, 15, 16, 16, 17, 17, 19, 20, 23, 27, 54,
        13, 14, 15, 16, 16, 17, 18, 19, 20, 23, 29, 59,
        13, 15, 15, 16, 16, 17, 18, 19, 20, 23, 30, 67,
        14, 15, 15, 16, 16, 17, 18, 19, 21, 24, 31,
        14, 15, 15, 16, 16, 17, 18, 19, 21, 24, 34]

# Calculate Median
median = np.median(data)

# Calculate Mode
mode = stats.mode(data)
mode_values = mode.mode.tolist()
mode_counts = mode.count.tolist()

# Calculate Quartiles (Q1 and Q3)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

# Calculate Percentiles (P10 and P95)
p10 = np.percentile(data, 10)
p95 = np.percentile(data, 95)

# Print the results
print("the Median is :", median)
# Print the mode and its counts (handling multiple modes)
print(" the Mode(s) is:", mode_values)
print("Frequency is:", mode_counts)
print("Q1 (25th percentile):", q1)
print("Q3 (75th percentile):", q3)
print("P10 (10th percentile):", p10)
print("P95 (95th percentile):", p95)
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Current date and time: {current_datetime}")