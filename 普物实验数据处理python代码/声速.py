# x=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5]
# y=[0.05536,0.05994,0.06468,0.06928,0.07402,0.07864,0.08310,0.08792,0.09266,0.09726]

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Given data
x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5])
#y = np.array([0.05536, 0.05994, 0.06468, 0.06928, 0.07402, 0.07864, 0.08310, 0.08792, 0.09266, 0.09726])
y = np.array([0.05530,0.06002,0.06466,0.06930,0.07394,0.07854,0.08312,0.08790,0.09246,0.09710])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Calculate the best fit line
y_fit = slope * x + intercept

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Original data')
plt.plot(x, y_fit, color='red', label=f'Fit line: y = {slope:.5f}x + {intercept:.5f}')

# Adding labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression of Given Data')
plt.legend()

# Display the plot
plt.show()
