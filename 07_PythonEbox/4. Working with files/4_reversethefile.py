# Python program to reverse the content of a file and store it in another file
def reverse_file_content(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            # Read the content of the file
            content = infile.read()
        # Reverse the content
        reversed_content = content[::-1]
        # Open the output file in write mode and write the reversed content
        with open(output_filename, 'w') as outfile:
            outfile.write(reversed_content)
        print(f"Content reversed and written to {output_filename}")
    except FileNotFoundError:
        print(f"The file {input_filename} does not exist.")
# Specify the input and output filenames
input_filename = "input.txt"
output_filename = "output.txt"
reverse_file_content(input_filename, output_filename)