"""
This file takes a collection of DNA sequences in FASTA format and returns the longest common subsequence.

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, 
you may return any single solution.)

Run this script by using the following command:
`python3 main.py fasta_file`
Where fasta_file is the path to your fasta file.
"""
import sys

def read_fasta(file: str) -> dict:
	"""
	This function reads a FASTA file and returns a dictionary of IDs and sequences.
	This function was taken from the 'gc' exercise.
	"""
	sequences = {}
	with open(file, "r", encoding="utf-8") as f:
		for line in f:
			if line.startswith(">"):
				sequence_id = line[1:].strip().rstrip()
				sequences[sequence_id] = ""
			else:
				sequences[sequence_id] += line.strip().rstrip()
	return sequences


def find_longest_common_subsequence(s1: str, s2: str) -> str:
	"""
	This function takes two dna sequences and returns the longest common subsequence.
	This function uses a dynamic programming approach.
	Improvement: search for ALL common substrings starting from a given length.
	"""
	m = len(s1)
	n = len(s2)
	matrix = [[0] * (n+1) for i in range(m+1)]
	max_len = 0
	end_index = 0
	result = {}

	for i in range(1, m+1):
		for j in range(1, n+1):
			if s1[i-1] == s2[j-1]:
				matrix[i][j] = matrix[i-1][j-1] + 1
				if matrix[i][j] > max_len:
					max_len = matrix[i][j]
					end_index = i
	return s1[end_index - max_len : end_index]	

		

	
def find_common_subsequences(dna_sequences: dict) -> set:
	"""
	This function takes a dictionary of id:dna_sequence and returns the longest common subsequence.
	how to return id also? to see which sequences have the subsequence in common?
	"""
	# Let's store the sequences in a set first to remove duplicates and allow for faster retrieval:
	sequences = list(dna_sequences.values())
	sequences.sort(key=len)
	print(sequences)
	

def main():
	fasta_file = sys.argv[1]
	print(find_common_subsequences(read_fasta(fasta_file)))
	cs = find_longest_common_subsequence("AACCCA", "CCCAAA")
	print(cs)

if __name__ == "__main__":
	main()
