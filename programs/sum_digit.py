'''
Write a function that computes the value of a+aa+aaa+aaaa 
with a given digit as the value of a.

Suppose the following input is supplied to the program: 9 
Then, the output should be: 11106 (i.e. 9+99+999+9999)
'''
def sum_a(a):
    numbers=[]
    numbers.append(a)
    for i in range(1,4):
        numbers.append(int(str(numbers[i-1])+str(a)))
    return sum(numbers)