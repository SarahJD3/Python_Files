"""
File name: kmerFinder.py
Author: Sarah Schoem
Created: 27Jan2024
Last Edit: 11Jun2025

"""

#Request for user input of sequence
print("Please enter  sequence of interest.")
#Example: sequence = "ATTACGAGCGGGACGGACGAGACCCGACGTA"
sequence = input("Sequence: ")
      
#Request for k-mer size
print("Please enter the size of the k-mers to find.")
#Example: k = 5
k = input("k-mer size: ")


# Initialize a dictionary to store k-mer counts and positions
kmer_counts = {}

# Iterate through the sequence
for i in range(len(sequence) - k + 1):
    kmer = sequence[i:i + k]
    if kmer in kmer_counts:
        kmer_counts[kmer]["count"] += 1
        kmer_counts[kmer]["positions"].append(i + 1)  # Adding 1 to make positions 1-based
    else:
        kmer_counts[kmer] = {"count": 1, "positions": [i + 1]}

# Print the k-mer table
print("K-mer    Position(s)    Count")
print("-----------------------------")
for kmer, info in kmer_counts.items():
    positions = ", ".join(map(str, info["positions"]))
    count = info["count"]
    print(f"{kmer}\t{positions}\t{count}")
