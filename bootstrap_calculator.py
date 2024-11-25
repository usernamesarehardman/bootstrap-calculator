import numpy as np

# Data set
weights = np.array([120, 140, 80, 100, 240])

# Set the number of bootstrap samples
n = 1000

# Generate means
means = []

for i in range(n):

	# Sample replacement
	sample = np.random.choice(weights, size=len(weights), replace=True)
	
	# Calculate mean of sample
	means.append(np.mean(sample))
	
# COnvert list to np array for indexing
means = np.array(means)

# Sort means
sorted_means = np.sort(means)

# Calculate 90% confidence interval
lower_bound = np.percentile(sorted_means, 5)
upper_bound = np.percentile(sorted_means, 95)

# Output
print(f"90% Confidence Interval for mean: ({lower_bound}, {upper_bound})")
