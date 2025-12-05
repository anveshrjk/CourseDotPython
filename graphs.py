# import numpy as np
# import matplotlib.pyplot as plt
#
# # Generate example data
# x = np.linspace(0, 10, 100)
# y = 2 * x + 5 + np.random.normal(0, 1, size=x.shape)  # Linear-like data with noise
#
# # Plot the scatter graph
# plt.figure(figsize=(8, 6))
# plt.scatter(x, y, color='blue', label='Data Points')
#
# # Fit a line using NumPy (degree 1 for linear)
# coeffs = np.polyfit(x, y, deg=1)
# fitted_y = np.polyval(coeffs, x)
# plt.plot(x, fitted_y, color='red', label='Fitted Line')
#
# # Print line coefficients
# slope, intercept = coeffs
# print(f"Slope: {slope:.2f}")
# print(f"Intercept: {intercept:.2f}")
#
# # Basic statistical analysis
# mean_y = np.mean(y)
# median_y = np.median(y)
# std_dev_y = np.std(y)
#
# print(f"Mean of Y: {mean_y:.2f}")
# print(f"Median of Y: {median_y:.2f}")
# print(f"Standard Deviation of Y: {std_dev_y:.2f}")
#
# # Add labels and show plot
# plt.title("Graph Analysis using Matplotlib and NumPy")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()
# plt.grid(True)
# plt.show()
