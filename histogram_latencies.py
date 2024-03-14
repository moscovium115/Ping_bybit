import matplotlib.pyplot as plt
import numpy as np


# import latencies from txt
latencies = []
with open('latencies.txt', 'r') as file:
    for line in file:
        latencies.append(float(line.strip()))

print(latencies)


plt.title('Latency Histogram')
plt.hist(latencies)
plt.show()

# statistics

# mean
mean = np.mean(latencies)
print('Mean:', mean)

# median
median=np.median(latencies)
print('Median:', median)

