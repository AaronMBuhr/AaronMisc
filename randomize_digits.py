import sys
import random

def randomize_digits(input_text):
    # Replace each digit with a random digit
    randomized_text = ''.join([str(random.randint(0, 9)) if char.isdigit() else char for char in input_text])
    return randomized_text

# Read input from stdin
input_text = sys.stdin.read()

# Process the input text
randomized_text = randomize_digits(input_text)

# Output the randomized text to stdout
print(randomized_text)

