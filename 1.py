#get the set of integers from the user
numbers = input("enter a set of integers seperated by space: ")
#split the input string into a list of integer
numbers_list = [int(num) for num in numbers.split()]
#calculate the average
average = sum(numbers_list) / len(numbers_list)
#print the result
print("the average of the set of integers is: ", average)