word_to_digit_mapping = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

input_string = "fourthreeseven1grvhrjxklh3ninetwothree"

# Replace alphabetical characters with their corresponding numeric digits
output_string = ''.join(word_to_digit_mapping.get(char, char) for char in input_string)

# Print the result
print(output_string)
