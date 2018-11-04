from sys import argv
import string

ones_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eightteen", "nineteen"]
tens_words = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
thousands_words = ["thousand", "million", "billion", "trillion", "quadrillion"]

print("Enter 'exit' to quit")

while (True):
    input_str = input("Number:").replace(',','') # Input will always be a string

    if input_str in ['quit', 'exit']:
        quit()

    if not input_str.isdigit():
        print("Error: input must be a positive integer")
        continue
    if len(input_str) > 15:
        print("Error: input cannot be larger than 15 digits")
        continue

    i = 0 # The digit position in the reversed number
    b = 0 # The position in the current block
    last_digit = 0
    output = []
    for c in reversed(input_str): # reversed() iterates through the string backward without creating a copy of the string
        digit = int(c)
        if b == 0 and (digit != 0 or len(input_str) == 1):
            output.append(ones_words[digit])
        elif b == 1 and digit != 0:
            if digit != 1:
                # Tens digit is at least 2
                output.append(tens_words[digit - 2])
            else:
                # Tens digit is a 1
                output[-1] = ones_words[last_digit + 10]
        elif b == 2 and digit != 0:
            output.append("hundred")
            output.append(ones_words[digit])

        i = i + 1
        b = i % 3
        if b == 0:
            output.append(thousands_words[i//3 - 1]) # The // operator performs integer division

        last_digit = digit

    print(" ".join(reversed(output)))
