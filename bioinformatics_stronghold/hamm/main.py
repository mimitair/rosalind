#! /mambaforge/envs/rosalind/bin/python

"""
This python script compares two DNA sequences of equal length
and calculates the Hamming distance between them (the corresponding
numbers of symbols that differ between both strings)
"""

import sys

def main():
    #TODO:
    # Make sure only one argument is passed
    
    # Read the file as an argument:
    file = sys.argv[1]
    
    # Open the file and read each line:
    with open(file, "r") as f:
        # Store sequences in a list:
        sequences = f.readlines()
        # Strip whitespaces and newlines:
        sequences = [x.strip() for x in sequences]
    
    # Compute hamming distance:
    hamming = hamming_distance(sequences[0], sequences[1])
                                        
    print(hamming)
    

def hamming_distance(sequence1: str, sequence2: str) -> int:
    # TODO:
    # Make sure sequences are of equal length
    # Make sure no unallowed characters are in the sequences

    # Initiate hamming distance at 0:
    hamming_distance = 0
    # zip the sequences will give [(sequence1.element1, sequence2.element2), (sequence1.element2, sequence2.element2),...]
    # Iterate over the zipped sequences
    for element1, element2 in zip(sequence1, sequence2):
        # If they are not equal, add 1 to the hamming distance:
        if element1.lower() != element2.lower():
            hamming_distance += 1
    
    return hamming_distance

    ### Alternative solution:
    # return sum([a != b for a, b in zip(s1, s2)])

    # To save memory:
    # return sum(a != b for a, b in itertools.izip(s1, s2))

if __name__ == "__main__":
    main()
