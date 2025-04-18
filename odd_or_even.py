"""
File name: odd_or_even.py
Author: Sarah Schoem
Created: 27Jan2024
Last Edit: 14Apr2025

"""

#Request for User to Enter a Number
print("Please type a number and this program will tell you if it is odd or even.")
print("Type 'q' to quit the program.")


while True:
    user_input = input("Enter a number: ")
    if user_input == 'q':
        print("Goodbye!")
        break
    
    try:
        number = int(user_input)
        #if and then statement
        if number % 2 == 0:
            print("Number is Even")
        else:
            print("Number is Odd")

    except ValueError:
        print("Please enter a valid number of type 'q' to quit.")

