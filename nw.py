from sys import argv
import string

# Max int = 9,223,372,036,854,775,807 
number_words = {
    "one":          1,
    "two":          2,
    "three":        3,
    "four":         4,
    "five":         5,
    "six":          6,
    "seven":        7,
    "eight":        8,
    "nine":         9,
    "ten":          10,
    "eleven":       11,
    "twelve":       12,
    "thirteen":     13,
    "fourteen":     14,
    "fifteen":      15,
    "sixteen":      16,
    "seventeen":    17,
    "eightteen":    18,
    "nineteen":     19,
    "twenty":       20,
    "thirty":       30,
    "forty":        40,
    "fifty":        50,
    "sixty":        60,
    "seventy":      70,
    "eighty":       80,
    "ninety":       90,
    "hundred":      100,
    "thousand":     1000,
    "million":      1000000,
    "billion":      1000000000,
    "trillion":     1000000000000,
    "quadrillion":  1000000000000000
}

thousand_powers = [x for x in number_words.keys() if number_words[x] >= 1000]

commas = False
debug = False

# Set flags according to command line arguments
for a in argv[1:]:
    if a[0] == '-' and len(a) > 1:
        for c in a[1:]:
            if c == 'c':
                commas = True
            if c == 'd':
                debug = True

print("Enter 'exit' to quit")

while (True):
    input_str = input("Words:")

    if input_str in ['quit', 'exit']:
        quit()

    input_list = input_str.replace('-',' ').replace(',','').lower().split()
    input_list = [x for x in input_list if x in number_words.keys()]

    if debug:
        print(input_list)
        print("Commas: " + str(commas))

    total = 0
    block = 0

    for i in range(len(input_list)):
        if input_list[i] in thousand_powers:
            # End the block
            total += block * number_words[input_list[i]]
            block = 0
        else:
            # Build the block
            if input_list[i] == "hundred":
                block *= 100
            else:
                block += number_words[input_list[i]]
                
        if i == len(input_list) - 1:
            # End of words
            total += block

    if commas:
        print("{:,}".format(total))
    else:
        print(total)