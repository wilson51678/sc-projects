"""
File: similarity.py
name: Wilson
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program compares short dna sequence, s2,
    with sub sequences of a long dna sequence, s1.
    In the end, the program with find the most match string in s1, which has the same length as 's2' and is consecutive.
    """
    old_dna = input('Please give me a DNA sequence to search: ')
    new_dna = input('What dna sequence would you like to match?')

    maximum = 0
    # i depends on the length of both strings, this step would help 'new_dna' check in 'old_dna' as consecutive string
    for i in range(len(old_dna)-len(new_dna)+1):
        # s1 is use for catching same length of characters as new_dna and transform into capital letter
        s1 = old_dna.upper()[i:i + len(new_dna)]
        counter = 0
        for j in range(len(new_dna)):
            # s2 is use for catching each character of 'new_dna' and transform into capital letter
            s2 = new_dna.upper()[j]
            if s2 == s1[j]:
                counter+=1
        # this step find which s1 match more characters with 'new_dna'
        if counter > maximum:
            maximum = counter
            ans = s1

    print('The best match is '+ans)




###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
