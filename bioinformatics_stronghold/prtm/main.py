"""
This script takes a file with a protein sequence on one line as an argument and returns its mass in Dalton.
How to run this script:
`python3 main.py test.txt`
Where test.txt contains the protein sequence. 
This script does not (yet) check if the given sequence is a valid one
"""
import sys

mass_table = {  'A': 71.03711, 
		'C': 103.00919, 
		'D':   115.02694, 
		'E':   129.04259,
		'F':   147.06841,
		'G':   57.02146,
		'H':   137.05891,
		'I':   113.08406,
		'K':   128.09496,
		'L':   113.08406,
		'M':   131.04049,
		'N':   114.04293,
		'P':   97.05276,
		'Q':  128.05858,
		'R':   156.10111,
		'S':   87.03203,
		'T':   101.04768,
		'V':   99.06841,
		'W':   186.07931,
		'Y':   163.06333
	     }

def calculate_mass(protein_sequence: str) -> float:
	# Initialize mass to 0
	total_mass = 0
	
	# Loop over the sequence and add the monoisotopic mass of each aa to the total mass
	for aa in protein_sequence:
		total_mass += mass_table[aa]
	
	# Return the total mass rounded to three decimals:
	return round(total_mass, 3)


def main():
	print("Reading the file...")
	file = sys.argv[1]
	with open(file, "r", encoding="utf-8") as f:
		protein_sequence = f.read().rstrip() # Stores sequence as a string
	print("Calculating mass...")
	print(f"Mass: {calculate_mass(protein_sequence)}")
	return None


if __name__ == "__main__":
	main()
