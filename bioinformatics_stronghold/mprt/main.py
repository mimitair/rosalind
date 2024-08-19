#!/home/mimitair/mambaforge/bin/python

import sys  # For accepting arguments passed in the CL
from urllib.request import urlopen  # To open data stored on the web through url
import regex as re  # Regular expressions (third-party package that provides methods to find overlapping sequences.

"""
To use this script run `python3 main.py <uniprot_id_file>` in the terminal. Uniprot ids should be on separate lines. 
For this assignment, we need to search for the n_glycosylation pattern, which I will hardcode here in regex format:
It means: First match "N", then any character that is not "P", then "S" or "T". Lastly any character that is not "P".
We assume that the fasta file contains no illegal character. So any character not "P" should be a different AA.
"""
n_glycosylation_regex ="N[^P][ST][^P]"

#TODO make regex more efficient with compile?
#TODO more doctests?

def read_uniprot_id_file(file) -> list:
	"""
	This function takes a txt file with uniprot ids on separate lines and returns them in a list
	
	DOCTSRING:
	>>> file = "test.txt"
	>>> read_uniprot_id_file(file)
	['A2Z669', 'B5ZC00', 'P07204_TRBM_HUMAN', 'P20840_SAG1_YEAST']
	"""
	# Open file for reading:
	file = open(file, "r")
	
	# Store each line as a string in a list
	lines = file.read().splitlines()
	
	# Close the file
	file.close()

	return lines

def retrieve_fasta(uniprot_id_list: list) -> dict:
	"""
	This function takes a list of uniprot ids and stores the corresponding FASTA sequence in a dictionary.
	"""
	# Specify the url. "{}" is where the id will come in
	url = 'http://www.uniprot.org/uniprot/{}.fasta'
	
	# Initiating empty dictionary to store the results:
	result = {}

	# Looping over every uniprot id and obtaining the fasta file through urllib
	for id in uniprot_id_list:
		# Strip the id of '_..._...' characters such that only the identifier is used:
		fasta_sequence = ""  # Empty string to store the sequence
		with urlopen(url.format(id.split("_", 1)[0])) as fasta_file:
			for line in fasta_file:
				# The file is read in bytes mode. We need to decode it first:
				# rstrip() to remove any newline characters at end of string.
				line = line.decode('utf-8').rstrip()
				# We don't need the first identifier line:
				if line.startswith('>'):
					continue
				else:
					fasta_sequence += line  # append to sequence

		# Store the id and the corresponding sequence in the dictionary:
		result[id] = fasta_sequence
	return result 

def find_motif(motif: str, protein_sequence: str) -> list:
	"""
	This function takes a specified motif and protein sequence and returns a list of the starting positions of the motif in the sequence
	For example motif "CAT" occurs at position 2 and 9 in the string "aCATggtaCATa". If the motif is not present, an empty list is returned.
	The motif should be given as a regex pattern.
	
	DOCTSRING:
	>>> find_motif('N[^P][ST][^P]', 'CCCNGSRFFFFFFFNHSNZSZ')
	[4, 15, 18]
	"""
	result=[]
	# using regex to find all motifs (with overlap) in the protein sequence:
	matches = re.finditer(motif, protein_sequence, overlapped=True)
	for match in matches:
		result.append(match.start()+1) # +1 because in the assignment indexing starts at 1 for some reason.
	return result

def main():
	# Capture the uniprot ID file from the argument passed in the CL.
	uniprot_id_file = sys.argv[1]
	
	# Read the uniprot id file and store as list
	ids = read_uniprot_id_file(uniprot_id_file)

	# Retrieve the sequences of each id and store in dictionary
	sequences = retrieve_fasta(ids)
	
	# Iterate over the sequences and look for the motif
	for id,sequence in sequences.items():
		start_indices = find_motif(n_glycosylation_regex, sequence)
		if len(start_indices) > 0:
			# If the list is not empty, print the start indices of each motif in the sequence with spaces:
			start_indices_string = ' '.join(map(str, start_indices))
			print(f'{id}\n{start_indices_string}')	 
		
	
if __name__ == "__main__":
	import doctest
	doctest.testmod()
	main()
