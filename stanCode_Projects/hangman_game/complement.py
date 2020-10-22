"""
File: complement.py
name: Wilson
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    TODO:
    """
    dna = input('Please give me a DNA strand and I will find the complement: ')
    up_dna = dna.upper()
    new_dna = build_complement(up_dna)
    print('The complement of '+up_dna+' is '+new_dna)


def build_complement(up_dna):
    """
    This function should replace words by roles:
    1. A,T replace to each other
    2. C,G replace to each other
    :param dna: str
    :return: ans
    """
    ans = ''
    # This step start replace characters to a new string
    for ch in up_dna:
        if ch == 'A':
            ans += 'T'
        elif ch == 'T':
            ans += 'A'
        elif ch == 'C':
            ans += 'G'
        elif ch == 'G':
            ans += 'C'
    return ans




###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
