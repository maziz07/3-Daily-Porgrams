# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello from Python!")

# Reading from the same file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
