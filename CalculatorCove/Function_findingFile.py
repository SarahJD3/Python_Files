"""
File name: Function_fingingFile.py
Author: Sarah Schoem
Created: 27Feb2024


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




import os

def filename_function():
    file_input = input("Enter a filename: ")
    while not os.path.exists(file_input):
        print("File not found.")
        file_input = input("enter a filename: ")
    print("File found, thanks")

def filename_function2():
    attempts = 0
    while attempts <5:
        file_input = input("Enter a filename: ")
        if os.path.exists(file_input):
            print("File found, thanks")
            return
        attempts+= 1
    print("Attempt", attempts, "Please check filename.")

def main():
    filename_function()
    filename_function2()


main()
