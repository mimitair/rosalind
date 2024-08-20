"""
This script takes a DNA string as input and returns the amount of A, C, G and T respectively.
A file containing the DNA sequence in txt format should be given as an argument.
Example:
`python3 main.py test.txt`
Where test.txt is the file containing one DNA sequence.
"""
import sys  # To take files as an argument

#TODO Check for valid unput


def count_nucleotides(dna_sequence: str) -> list:
	return [dna_sequence.count('A'), dna_sequence.count('C'), dna_sequence.count('G'), dna_sequence.count('T')]

def main():
	# Capture the file given as an argument in the command line:
	file = sys.argv[1]
	
	# Open the file and store the sequence as a string:
	with open(file, 'r') as f:
		sequence = f.read()
	
	count = count_nucleotides(sequence)
	# Print the count of nucleotides to the screen:
	print(f"Amount of A: {count[0]}\nAmount of C: {count[1]}\nAmount of G: {count[2]}\nAmount of T: {count[3]}")			
	
	return None
	

if __name__ == "__main__":
	main()
