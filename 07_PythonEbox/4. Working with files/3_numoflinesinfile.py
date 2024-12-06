 # Python program to count the number of lines in a file
def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            print(f"The file has {line_count} lines")
    except FileNotFoundError:
        print("The specified file does not exist.")
# Specify the filename
filename = "input.txt"
count_lines_in_file(filename)  