import matplotlib.pyplot as plt
import numpy as np


# import latencies from txt
latencies = []
with open('latencies.txt', 'r') as file:
    for line in file:
        latencies.append(float(line.strip()))

print(latencies)

latencies = np.array(latencies)/(10e5)



plt.title('Latency Histogram')
plt.hist(latencies,bins=30)
plt.show()

# statistics

# mean
mean = np.mean(latencies)
print('Mean:', mean)

# median
median=np.median(latencies)
print('Median:', median)

# 99th percentile:
percentile_99 = np.percentile(latencies, 99)
print('99th percentile:', percentile_99)

#minimum and maximum
minimum = np.min(latencies)
print('Minimum:', minimum)

maximum = np.max(latencies)
print('Maximum:', maximum)

