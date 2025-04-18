"""
File name: amino_acid_list.py
Author: Sarah Schoem
Created: 04Feb2024
Last Edit: 17Apr2025

"""

print("This program contains a list of 5 amino acids.")
print("Please select a number 1-5 to reveal the amino acid in the list.")
print("Type 'q' to quit the program.")

# Amino acids list
amino_acids = ["Trp", "Arg", "Liu", "Ilu", "Asp"]


# Prompt user for input
while True:
    user_input = input(f"Enter a number between 1 and {len(amino_acids)}(or 'q' to quit): ")
    
    if user_input == 'q':
        print("Goodbye!")
        break

    try:
        index = int(user_input)
        if 1 <= index <= len(amino_acids):
            print(f"The corresponding amino acid is: {amino_acids[index - 1]}")
        else:
            print("Error: Please enter a number within the specified range.")
                
    except ValueError:
        print("Error: Please enter a valid integer or 'q' to quit.")


