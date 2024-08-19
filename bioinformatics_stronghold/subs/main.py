#! /mambaforge/envs/rosalind/bin/python

"""
This python script takes two sequences as input and checks if the second sequence is a subsequence of
the first one (a motif). If yes, it returns the position(s) in the first string that contains the substring. 
"""

import sys
import re

def main():
    # Read in the file as an argument:
    file = sys.argv[1]
    # Open the file and read each line:
    with open(file, "r") as f:
        # Store sequences in a list (assuming each sequence only populates one line):
        sequences = f.readlines()
        # Strip whitespaces and newlines:
        sequences = [x.strip() for x in sequences]
    
    # Define the sequence and the subsequence:
    sequence = sequences [0]
    subsequence = sequences[1]

    # We use regex to solve this problem.
    pattern = "(?={})".format(re.escape(subsequence))
    indices = [m.start() + 1 for m in re.finditer(pattern, sequence)] 
    
    # Print indices separated by space
    print(" ".join(map(str, indices)))  


    """
    CHATGPT explanation:

    pattern = "(?={})".format(re.escape(subsequence)):

        re.escape(subsequence): This function escapes special characters in the subsequence string. 
        It is essential to escape these characters because they may have special meanings in regular expressions. 
        For example, if your subsequence contained characters like ".", "*", or "+", they would have special meanings in regular expressions. 
        Escaping ensures that these characters are treated as literal characters in the regular expression pattern.
    
        "(?={})".format(...): This string formatting technique replaces {} in the pattern with the escaped subsequence string. 
        The resulting pattern is a positive lookahead assertion (?=...) where ... represents the escaped subsequence. 
        A positive lookahead assertion checks if a particular pattern occurs ahead in the string without consuming it. 
        So, (?=...) ensures that the pattern contained within the lookahead matches at the current position in the string, without actually consuming any characters. 
        This is useful for finding overlapping matches.


    indices = [m.start() + 1 for m in re.finditer(pattern, sequence)]:

        re.finditer(pattern, sequence): 
        This function searches for all non-overlapping matches of the pattern in the sequence string. 
        It returns an iterator yielding MatchObject instances for each match found.
        
        [m.start() + 1 for m in re.finditer(pattern, sequence)]: 
        This list comprehension iterates over the matches found by re.finditer(). 
        For each match (m), it retrieves the starting index of the match (m.start()) and adds 1 to it (m.start() + 1). 
        This adjustment ensures that the indices start from 1 as required by the assignment.
        print(" ".join(map(str, indices))):


    map(str, indices): 

        This applies the str function to each element of indices, converting each index to a string.
        " ".join(...): This joins the strings in the iterable (resulting from map(str, indices)) using a space character as the separator.
        print(...): Finally, this prints the resulting string of indices, separated by spaces.



    ALTERNATIVE SOLUTION:
    s1,s2 = open('rosalind_subs.txt').read().split('\r\n')

    for i in range(len(s1)):
        if s1[i:].startswith(s2):
            print i+1,
    """




if __name__ == "__main__":
    main()
