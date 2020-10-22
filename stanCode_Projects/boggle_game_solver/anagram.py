"""
File: anagram.py
Name: Wilson Wang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


# Global various
count = 0                     # count the number of vocabs in the list
lst = []                      # This list contain of answers for anagrams searching


def main():
    global count, lst
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")

    while True:
        anagram = input('Find anagrams for: ').lower()
        # check the user enter a vocab and set the break as constants 'EXIT'
        if anagram != EXIT:
            print('Searching...')
            find_anagrams(anagram)
            print(str(count)+' anagrams: '+str(lst))

            # reset the global various for next anagram searching
            lst = []
            count = 0
        else:
            break


def read_dictionary():
    """
    This function will create a list which contain all data in file.
    :return: list,  sort out the 'FILE' as a list for anagrams searching
    """
    with open(FILE, 'r') as f:
        dictionary = []
        # separate file into lines
        for line in f:
            # separate line into list
            word_list = line.split()
            # separate vocab in list
            for word in word_list:
                dictionary.append(word)
    return dictionary


def find_anagrams(s):
    """
    This function should start helper function
    :param s: string, the anagrams for searching
    :return: None
    """
    # set the dictionary as list and add into helper function as parameter to decrease searching time
    dict = read_dictionary()
    # set a helper function to use backtracking
    find_anagrams_helper(s, '', dict, '')


def has_prefix(s, index, dict):
    """
    This function should search the sub string of anagrams in dictionary to decrease searching time.
    :param sub_s: str, a string contain above 2 words for key word searching in dictionary
    :return: boolean
    """

    sub_s = ''
    for i in index:
        sub_s += s[int(i)]

    # get every vocab from dictionary
    for vocab in dict:
        # check the sub_s in vocab
        if vocab.startswith(sub_s):
            return True
    return False


def find_anagrams_helper(s, chosen, dict, index):
    """
    This function use back tracking to find the answers of anagrams
    :param s: string, the anagrams for searching
    :param chosen: string, the answer of anagrams
    :param dict: list, storage all the chosen in a list
    :param index: string, storage index number for chosen
    :return: None
    """
    global count, lst
    # base_case
    if len(index) == len(s):

        for i in index:
            chosen += s[int(i)]
        if chosen in dict and chosen not in lst:
            print('Found: '+chosen)
            print('Searching...')

            # add result in global various
            count += 1
            lst.append(chosen)
    # recursive_case
    else:
        for i in range(len(s)):
            if str(i) in index:
                pass
            else:
                # pre-check the anagrams in dictionary to decrease searching times when the length of chosen above 2
                if len(index) >= 2 and has_prefix(s, index, dict):
                    # choose
                    index += str(i)
                    # explore
                    find_anagrams_helper(s, chosen, dict, index)
                    # un-choose
                    index = index[:len(index)-1]

                elif len(index) < 2:
                    # choose
                    index += str(i)
                    # explore
                    find_anagrams_helper(s, chosen, dict, index)
                    # un-choose
                    index = index[:len(index)-1]
                else:
                    return


if __name__ == '__main__':
    main()
