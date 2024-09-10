def is_multiple(n):
    if n%5==0 and n%7==0:
        return True
    else:
        return False
num = int(input("enter an integer: "))
if is_multiple(num):
    print(num, "is a multiple of 5 and 7.")
else:
    print(num, "is not a multiple of 5 and 7.")