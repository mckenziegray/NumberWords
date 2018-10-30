# NumberWords
This program converts words representing numbers into their numerical form, and vice-versa:

Twenty-one billion nineteen million eight hundred forty thousand five hundred seventy-two <--> 21019840572

### Usage
`python nw.py [-c]`

### Important Notes
* Decimals and negative numbers are not currently supported, but probably will be in the future.
* Only supports numbers up to 999,999,999,999,999 (one less than one quintillion). This program's implementation requires an arbitrary cutoff point, and the quintillions begin to exceed the capacity of a 64-bit integer.

## Words to Numbers
### Format
Words must be provided in a proper order and format. All words must be separated by either a space or a hyphen (-) and they must be ordered and spelled correctly. Note that case does not matter and extra words such as "and" are fine and will be stripped out. 

Examples of **correct** format:
* `three`
* `four hundred and twenty-six`
* `Six Hundred Thousand`
* `three hundred sixty seven billion four hundred million six thousand forty`

Examples of **incorrect** format:
* `one thousand four million` ("Thousand" cannot proceed "million")
* `hundred thousand` (A number must proceed "hundred," such as "one hundred" or "four hundred")
* `one forty seven` (If the intention is to represent the number 147, the word "hundred" must be included, such as "one hundred forty seven")

Using incorrect format will result in undefined behavior.

### Command line options
If the comma flag `-c` is enabled, results will be formatted with comma separation.

Without `-c`: 21019840572

With `-c`: 21,019,840,572

## Numbers to Words
Not yet implemented.
