# QAC_Challenges
-1-

julydevops.py

Write a python script with the above name which does the following:

- initialises a list which contains the FIRST NAME of all 21 people in this cohort
- using the .append() function add me to the list
- print the 5th person in the list (this is a trick question, what is special about the way Python indexes?)
- print the number of Chris in the cohort

Once you have a solution, remember to push it to github.

-2-

timestable.py

Make a python script with the above name which solves the following challenge: 

https://portal.qa-community.co.uk/~/devops/challenges/times-table-grid

Given an integer n, write a python function which returns a times table grid for all the integers between 1 and n.
The grid should be separated by tabs and new lines.

For example, given n = 4 it should return the grid

1   2   3   4
2   4   6   8
3   6   9   12
4   8   12  16

given n=7 it should return

1   2   3   4   5   6   7   
2   4   6   8   10  12  14  
3   6   9   12  15  18  21  
4   8   12  16  20  24  28  
5   10  15  20  25  30  35  
6   12  18  24  30  36  42  
7   14  21  28  35  42  49  

-3-

I have a function called `string_gen()` that will return a random 5-character-long string of lowercase letters. Write some tests for this function. 

To reiterate, the output should always be:
	
- a string
- 5 characters long
- comprised of lowercase letters


-4-
Define a class named Rectangle, which can be constructed by a length and width.

The Rectangle class needs to have a method that can compute area.

Finally, write a unit test to test this method.


-5-

Write a function that accepts a sequence of whitespace separated words as a string input, sorts each item alphanumerically and removes any duplicate items, then returns the result as a string. 
Write a test for this function.

Suppose the following input is supplied to the program: 

    hello world and practice makes perfect and hello world again

Then, the output should be: 

    again and hello makes perfect practice world

Hint: make use of the set() collection type!

-6-

Write a function that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

 

Suppose the following input is supplied to the program: 9 Then, the output should be: 11106 (i.e. 9+99+999+9999)
 

Write a test for this function

-7-

sevenNotFive.py

Create a python function in the file above which satisfies the following challenge:

https://portal.qa-community.co.uk/~/devops/challenges/seven-not-five

Write a program to:

find all numbers, between 2000 and 3200 (both included), that are divisible by 7, but are not a multiple of 5
The numbers obtained should be returned on a single line. seperated by commas.

-8-

amsterdam.py

Given a string, return the number of times "am" appears in the string BUT ONLY WHEN "am" is not followed or preceded by any other LETTERS.
 
eg

name("Am I in Amsterdam") → 1
name("I am in Amsterdam am I?") → 2
name("I have been in Amsterdam") → 0

 
you should also attempt to write some tests for this function.