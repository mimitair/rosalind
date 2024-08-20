"""
This script takes a DNA sequence as input and returns the reverse complement of that string.
The reverse complement of a DNA string s is the string s_c formed by reversing the symbols of s, 
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
How to run this script:
`python3 main.py test.txt`
Where test.txt contains the DNA sequence on one line.
"""

import sys

def reverse_complement(dna_string):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}  # Define the complement for each base
    reverse = dna_string[::-1]  # Reverse the string
    complemented = [complement[base] for base in reverse]
    return ''.join(complemented)

def main():
	file = sys.argv[1]
	with open(file, "r") as f:
		dna_sequence = f.read().rstrip()
	
	# Take reverse complement and print to screen:
	print(reverse_complement(dna_sequence))


if __name__ == "__main__":
	main()

