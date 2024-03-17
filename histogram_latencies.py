import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# import latencies from txt
latencies = []
with open('latencies.txt', 'r') as file:
    for line in file:
        latencies.append(float(line.strip()))

latencies = np.array(latencies) / 1e6  # Convert to seconds

# Fit exponential distribution
loc, scale = stats.expon.fit(latencies)

# Generate x values for plotting the fitted exponential distribution
x_values = np.linspace(0, max(latencies), len(latencies))

# Calculate the corresponding PDF values for the fitted exponential distribution
pdf_values = stats.expon.pdf(x_values, loc, scale)

plt.title('Latency Histogram')
# Plot histogram of the data
plt.hist(latencies, bins=180, density=True, alpha=0.5, label='Data Histogram')

# Plot the fitted exponential distribution
plt.plot(x_values, pdf_values, 'r--', label='Exponential Distribution')

plt.xlabel('Latency (ms)')
plt.ylabel('Density')
plt.legend()
plt.show()

# statistics

# mean
mean = np.mean(latencies)
print('Mean:', mean)

# median
median = np.median(latencies)
print('Median:', median)

# 99th percentile:
percentile_99_9 = np.percentile(latencies, 99.9)
print('99.9th percentile:', percentile_99_9)

# minimum and maximum
minimum = np.min(latencies)
print('Minimum:', minimum)

maximum = np.max(latencies)
print('Maximum:', maximum)
print("number of samples:", len(latencies))
