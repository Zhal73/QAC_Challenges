"""
    Write a function that accepts a sequence of whitespace separated words as a string input, sorts each item alphanumerically and removes any duplicate items, then returns the result as a string. 
    Write a test for this function.

    Suppose the following input is supplied to the program: 

        hello world and practice makes perfect and hello world again

    Then, the output should be: 

        again and hello makes perfect practice world

    Hint: make use of the set() collection type!
"""

def sort_string(input):
    #change the input string into lowercase
    #split the input string into a list where each word is an element of the list
    record=input.lower().split()  

    #transform the list into a set, so duplicates are removed
    set_string=set(record)

    #make a list again so it can be ordered, because Sets are unordered
    record=list(set_string)
    record.sort() 

    #creates the result string by concatenating each word
    result=""
    for word in record:
        result=result + word +" "
    return(result.rstrip()) #rstrip() removes last space

    