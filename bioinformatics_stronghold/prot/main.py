#! /mambaforge/envs/rosalind/bin/python

import sys

def main():
    # Specify the file as argument:
    file = sys.argv[1]

    # Read file contents, store each line as element of list and remove whitespaces:
    with open(file, "r", encoding="utf-8") as f:
        rna = f.read().splitlines()

    # Join the elements of the list into one string:
    rna = "".join(rna)

    # Translate the string:
    protein = rna_to_protein(rna)

    print(protein)


def rna_to_protein(rna_sequence:str) -> str:
    # Define a codon dictionary:

    codon_table = {
    'UCA': 'S',    # Serina
    'UCC': 'S',    # Serina
    'UCG': 'S',    # Serina
    'UCU': 'S',    # Serina
    'UUC': 'F',    # Fenilalanina
    'UUU': 'F',    # Fenilalanina
    'UUA': 'L',    # Leucina
    'UUG': 'L',    # Leucina
    'UAC': 'Y',    # Tirosina
    'UAU': 'Y',    # Tirosina
    'UAA': '*',    # Stop
    'UAG': '*',    # Stop
    'UGC': 'C',    # Cisteina
    'UGU': 'C',    # Cisteina
    'UGA': '*',    # Stop
    'UGG': 'W',    # Triptofano
    'CUA': 'L',    # Leucina
    'CUC': 'L',    # Leucina
    'CUG': 'L',    # Leucina
    'CUU': 'L',    # Leucina
    'CCA': 'P',    # Prolina
    'CCC': 'P',    # Prolina
    'CCG': 'P',    # Prolina
    'CCU': 'P',    # Prolina
    'CAC': 'H',    # Histidina
    'CAU': 'H',    # Histidina
    'CAA': 'Q',    # Glutamina
    'CAG': 'Q',    # Glutamina
    'CGA': 'R',    # Arginina
    'CGC': 'R',    # Arginina
    'CGG': 'R',    # Arginina
    'CGU': 'R',    # Arginina
    'AUA': 'I',    # Isoleucina
    'AUC': 'I',    # Isoleucina
    'AUU': 'I',    # Isoleucina
    'AUG': 'M',    # Methionina
    'ACA': 'T',    # Treonina
    'ACC': 'T',    # Treonina
    'ACG': 'T',    # Treonina
    'ACU': 'T',    # Treonina
    'AAC': 'N',    # Asparagina
    'AAU': 'N',    # Asparagina
    'AAA': 'K',    # Lisina
    'AAG': 'K',    # Lisina
    'AGC': 'S',    # Serina
    'AGU': 'S',    # Serina
    'AGA': 'R',    # Arginina
    'AGG': 'R',    # Arginina
    'GUA': 'V',    # Valina
    'GUC': 'V',    # Valina
    'GUG': 'V',    # Valina
    'GUU': 'V',    # Valina
    'GCA': 'A',    # Alanina
    'GCC': 'A',    # Alanina
    'GCG': 'A',    # Alanina
    'GCU': 'A',    # Alanina
    'GAC': 'D',    # Acido Aspartico
    'GAU': 'D',    # Acido Aspartico
    'GAA': 'E',    # Acido Glutamico
    'GAG': 'E',    # Acido Glutamico
    'GGA': 'G',    # Glicina
    'GGC': 'G',    # Glicina
    'GGG': 'G',    # Glicina
    'GGU': 'G'     # Glicina
    }

    # Initialize empty string:
    amino_acid_sequence = ""

    # Iterate over the rna_sequence in steps of 3
    for i in range(0, len(rna_sequence), 3):
        # Define the codon:
        codon = rna_sequence[i:i+3]
        # If a stop codon is encountered we stop:
        if codon == "UAG" or codon == "UGA" or codon == "UAA":
            break
        # Get the codon from the codon table. If it cannot find it, it returns an empty string ''
        amino_acid = codon_table.get(codon, '')
        amino_acid_sequence += amino_acid
    
    return amino_acid_sequence

if __name__ == "__main__":
    main()

