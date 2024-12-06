try:
    x = int(input("Enter number 1\n"))
    y = int(input("Enter number 2\n"))
    result = x / y
    print(result)
except ZeroDivisionError:
    print("Divide By Zero Error")