#! /mambaforge/envs/rosalind/bin/python

"""
This python script takes a fasta file with multiple sequences and returns the ID
of the string with the highest GC content.
"""

import sys

def main():
    # TODO:
    # Limit number of arguments to 1

    # Define the fasta file as the first argument:
    fasta_file = sys.argv[1]

    # Store the sequences in a dictionary:
    sequences_dict = parse_sequences(fasta_file)

    # Extract the ID and GC content of the sequence with the highest GC content:
    result = extract_highest_gc(sequences_dict)

    # Print result to stdo:
    print(f"{result[0]}\n{result[1]}")

    
def parse_sequences(fasta_file) -> dict:
    # This function reads a fasta file and returns the sequences and their ID in a dictionary format
    # TODO:
    # Make sure the same ID cannot occur twice in the dict.
    # Check for correct input (only A, G, C and T)

    # Initiate empty dictionary:
    sequences = {}
    # Open the file:
    with open(fasta_file, "r") as f:
        # Iterate over each line:
        for line in f:
            # Remove leading and traling white spaces:
            line = line.strip()
            # Store a new sequence id if the line starts with ">":
            if line.startswith(">"):
                sequence_id = line[1:].strip()
                sequences[sequence_id] = ""
                continue
            # If line does not start with ">", simply append the line to the key value as a string
            sequences[sequence_id] += line

    return sequences

def compute_gc_content(dna_sequence: str) -> float:
    # This function computes the GC content of a given DNA string
    sequence_length = len(dna_sequence)
    gc_amount = 0
    # iterate over the sequence
    for base in dna_sequence:
        # if base is g or c, add one to the counter
        if base.lower() in "gc":
            gc_amount += 1
    return gc_amount/sequence_length

def extract_highest_gc(dna_sequences: dict) -> tuple:
    # This function iterates over the dictionary, calculates the GC content and returns the ID of the sequence
    # with the highest GC content, along with its GC content

    #Initiate empty dictionary to store the gc contents with ID as keys:
    gc_dict = {}
    # Iterate over keys and values of the dictionary:
    for sequence_id, sequence in dna_sequences.items():
        gc_content = compute_gc_content(sequence)
        gc_dict[sequence_id] = gc_content
    
    # Now we need to find the highest value in the dictionary and return its key and the value:
    max_key = max(gc_dict, key = lambda x: gc_dict[x])
    max_value = max(gc_dict.values()) * 100


    return max_key, max_value


if __name__ == "__main__":
    main()
