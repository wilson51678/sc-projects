"""
File: hailstone.py
Name: Wilson Wang
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, as defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

STOP = 1

def main():
    """
    This program should implement a console program that simulates
    the execution of the Hailstone sequence, as defined by Douglas
    Hofstadter. Output format should match count the steps that program runs to reach 1.
    """
    print('This program computes Hailstone sequences')
    random = int(input('Enter a number:'))
    # program should stop at here
    if random == STOP:
        print('It took 0 step to reach 1')
    # program should continue compute
    else:
        step = 0
        while True:
            # when the number is even, the number would compute in the equation and count step
            if random%2 == 0:
                even = random // 2
                print(str(random)+' is even, so I take half :'+str(even))
                random = even
                step+=1
            # program would stop at here
            elif random == STOP:
                break
            # when the number is odd, the number would compute in the equation and count step
            else:
                odd = (3 * random) + 1
                print(str(random)+' is odd, so I make 3n+1 :'+str(odd))
                random = odd
                step+=1
        # this code shows the steps to reach 1
        print('It took '+str(step)+' steps to reach 1')



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
