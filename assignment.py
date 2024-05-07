#Assignment


'''ques1.)Q1. Create a python program to sort the given list of tuples based on integer value using a
lambda function.
[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
'''
lst=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
lst.sort(key=lambda x:x[1])
print(lst)




'''
Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using
lambda and map functions.
'''
lst=[1,2,43,12,31,13,14]
list(map(lambda x:x**2,lst))
print(list(map(lambda x:x**2,lst)))



'''
Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and
lambda functions
Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
'''
lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple(map(lambda x:str(x),lst))
print(tuple(map(lambda x:str(x),lst)))


'''
Q4. Write a python program using reduce function to compute the product of a list containing numbers
from 1 to 25.
'''
lst=list(range(1,26))
print(lst)
from functools import reduce
print(reduce(lambda x,y:x*y,lst))



'''
Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the
filter function.
[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
'''
lst=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
print(list(filter(lambda x:x%2==0 and x%3==0,lst)))


'''
Q6. Write a python program to find palindromes in the given list of strings using lambda and filter
function.

'''
lst=["hello","neha","php", "science","pyhton","radar","naman"]
print(list(filter(lambda x:x==x[::-1],lst)))
print(reduce(lambda x,y:x+y,lst))
