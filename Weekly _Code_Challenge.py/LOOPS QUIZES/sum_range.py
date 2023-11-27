# Find the sum of the even numbers from 10 to 100 (including 10 and 100)

# Initialize a variable to store the sum
sum_of_evens = 0

# Iterate through numbers from 10 to 100
for num in range(10, 101):
    # Check if the number is even
    if num % 2 == 0:
        # Add the even number to the sum
        sum_of_evens += num

# Print the result
print("The sum of even numbers from 10 to 100 is:", sum_of_evens)
