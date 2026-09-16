import random

# Generate a list of 5 random floating-point numbers between 0 and 10
random_floats = [random.uniform(0, 10) for _ in range(5)]

# Calculate the minimum and maximum values using built-in functions
min_value = min(random_floats)
max_value = max(random_floats)

# Print the generated list and the results
print("Generated List:", random_floats)
print(f"Minimum Value: {min_value}")
print(f"Maximum Value: {max_value}")
