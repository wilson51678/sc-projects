"""
File: caesar.py
name: Wilson
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program demonstrates the idea of caesar cipher.
    Users will be asked to input a number to produce shifted
    ALPHABET as the cipher table. After that, any strings typed
    in will be encrypted.
    """
    secret = int(input('Secret number: '))
    string = input("What's the ciphered string? " )
    # This step insure string is made by capital letters
    up_string = string.upper()
    new_alphabet = build_new(secret)
    deciphered = find_old(up_string,new_alphabet)
    print('The deciphered string is: ' + str(deciphered))


def build_new(secret):
    """
    This function will make a new line of alphabet, the first character should be choose by ' secret'
    :param secret: int, secret >= 0
    :return: ans: str
    """
    new = ''
    # when secret = 0, this step should skip
    if secret >= 1:
        # This step from a new line of alphabet , and the first character determined by 'secret'
        for i in range(secret):
            ch = ALPHABET[i+len(ALPHABET)-secret]
            new+=ch
    # This step should finish the rest of line of alphabet
    for i in range(len(ALPHABET)-secret):
        ch = ALPHABET[i]
        new+=ch

    return new


def find_old(up_string,new_alphabet):
    """
    This function should use each character of 'up_string' to finds the location at 'new_alphabet' and encrypts the
    answer from 'Alphabet'
    :param up_string: str, The string that user type for decipher
    :param new_alphabet: str, the rearrange alphabet string, which decided by SECRET
    :return: ans: str, The string after deciphered
    """
    ans=''
    # This step should use both new_alphabet and Alphabet to find the answer
    for i in range(len(up_string)):
        ch = up_string[i]
        if ch.isalpha():
            # use each character to find the number at new_alphabet and use the number to find the character in Alphabet
            ans += ALPHABET[new_alphabet.find(ch)]
        else:
            ans += ch
    return ans





#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
