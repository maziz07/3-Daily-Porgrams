def reverse_file_content(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
    with open(output_file, 'w') as file:
        file.write(content[::-1])

# Test the function
input_file_path = "example.txt"  # Replace with your file path
output_file_path = "reversed_example.txt"  # Output file
reverse_file_content(input_file_path, output_file_path)
