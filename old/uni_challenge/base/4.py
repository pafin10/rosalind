with open("4.txt", "r") as file:
    with open('output.txt', 'w') as output_file:
        for line_number, line in enumerate(file, start=1):
            if line_number % 2 == 0 and line.strip():
                output_file.write(line)

# Print the contents of the output file for verification
with open('output.txt', 'r') as output_file:
    for line in output_file:
        print(line.strip())
