"""
File name: Sum_Avg_Calculator.py
Author: Sarah Schoem
Created: 04Feb2024
Last Edit: 18Apr2025

"""

# place holder
total_sum = 0

# user entry
for i in range(3):
    num = float(input(f"Enter number {i+1}: "))
    total_sum += num

# average
average = total_sum / 3

# Displaying sum and average
print(f"Sum of the numbers: {total_sum}")
print(f"Average of the numbers: {average:.2f}")
