'''
Write a function called ‘calculate_mean’ that takes a list of numbers as input and 
returns the mean (average) of the numbers. The function should calculate the mean 
using the sum of the numbers divided by the total count.

'''



def my_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean


data = [11,2,3,23,45,33,23,23,45,33,33,1,2,3]
mean_value = my_mean(data)
print("Mean:", mean_value)
