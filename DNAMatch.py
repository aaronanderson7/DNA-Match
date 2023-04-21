# Name: Aaron Anderson
# Class: CS325 (Analysis of Algorithms)
# Assignment: 3
# Date: 04/24/2023
# Description: Answer the Assignment 3 Homework Questions using Dynamic Programming.


#-------------------------- Question 1a ---------------------------------------


def dna_match_topdown_helper(D1, D2, m, n):
    """
    Recursive helper function for dna_match_topdown function.
    :param D1: input DNA sequence - string of A, C, G, T
    :param D2: input DNA sequence - string of A, C, G, T
    :param m: length of DNA sequence - integer
    :param n: length of DNA sequence - integer
    :return: recursive function calls
    """
    # CITATION: code from Module 3 Exploration 3.3

    if m < 0 or n < 0:
        return 0
    elif D1[m] == D2[n]:
        return (1 + dna_match_topdown_helper(D1, D2, m - 1, n - 1))
    else:
        return max(dna_match_topdown_helper(D1, D2, m - 1, n), dna_match_topdown_helper(D1, D2, m, n - 1))


def dna_match_topdown(DNA1, DNA2):
    """
    The dna_match_topdown function uses a top-down dynamic programming approach
    to find the longest matching string between two input DNA sequences.
    :param DNA1: input DNA sequence - string of A, C, G, T
    :param DNA2: input DNA sequence - string of A, C, G, T
    :return: length of longest continuous length of DNA string alignment (and sequence).
    """
    # CITATION: code from Module 3 Exploration 3.3

    return dna_match_topdown_helper(DNA1, DNA2, (len(DNA1) - 1), (len(DNA2) - 1))


s1 = "ATAGTTCCGTCAAA"
s2 = "GTGTTCCCGTCAAA"

print(dna_match_topdown(s1, s2))



#-------------------------- Question 1b ---------------------------------------




#-------------------------- Question 2a ---------------------------------------




#-------------------------- Question 2a ---------------------------------------






#--------------------------    TESTS     ---------------------------------------



# TEST FOR 1A

s1 = "ATAGTTCCGTCAAA"
s2 = "GTGTTCCCGTCAAA"

print(dna_match_topdown(s1, s2))