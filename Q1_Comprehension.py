'''


 Write a function that takes a list of numbers as input and returns a new list containing 
 only the even numbers from the input list. Use list comprehension to solve this problem.


'''


input = [1,2,3,4,5,6,7,8,9,10]
result = [x for x in input if x%2 == 0]
print(result)