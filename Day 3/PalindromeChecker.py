def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char for char in s if char.isalnum()).lower()
    # Check if the string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]

# Test the function
test_string = "A man, a plan, a canal, Panama"
print(f"Is '{test_string}' a palindrome? {is_palindrome(test_string)}")
