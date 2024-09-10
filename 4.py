def fibonacci(n):
    series = [0,1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series

num_terms = int(input("enter the number of terms: "))
print("the fibonacci series upto", num_terms, "terms is: ", fibonacci(num_terms))