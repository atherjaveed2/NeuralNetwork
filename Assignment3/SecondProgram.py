import numpy as np

# Create a random vector of size 20 with floats in the range 1-20
random_vector = np.random.uniform(1, 20, 20)

# Reshaping the array to 4 by 5 size (4*5)
reshaped_array = random_vector.reshape(4, 5)
print("\nReshaped Array Before:")
print(reshaped_array)

# Replace the max in each row with 0
reshaped_array[np.arange(4), reshaped_array.argmax(axis=1)] = 0

# Print the reshaped array after replacing max value in row with 0.
print("\nReshaped Array After:")
print(reshaped_array)
