def main():
    try:
        a = (input("Enter number 1\n"))
        b = (input("Enter number 2\n"))
        x=int(a)
        y=int(b)
        result = x / y
        print(result)
    except ZeroDivisionError:
        print("Divide By Zero Error")
    except ValueError:
        print("Invalid Value")
if __name__== "__main__":
    main()