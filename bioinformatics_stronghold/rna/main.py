"""
This script takes a DNA sequence as input and returns the translated RNA sequence.
DNA sequences are provided as one line in a .txt file as an argument in the command line. For example:
`python3 main.py test.txt`
Where test.txt contains the DNA sequence.
"""

import sys

def dna_to_rna(dna_sequence: str) -> str:
	return dna_sequence.replace("T", "U")

def main():
	# Capture the file as the first argument:
	file = sys.argv[1]
	
	# Open the file and read the dna sequence
	with open(file, "r") as f:
		dna_sequence = f.read()
	
	# Print the translated dna sequence:
	print(dna_to_rna(dna_sequence))

	return None

if __name__ == "__main__":
	main()
