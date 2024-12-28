import argparse
import hashlib

parser = argparse.ArgumentParser(description="Solution to 2015 Day 5 – Part 1")
parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
parser.add_argument("-t", "--target-sum", help="Target sum")
args = parser.parse_args()

strings = []

with open(args.input_file, mode="r") as reader:
    for line in reader:
        strings.append(line)

nice_strings = []

for string in strings:
    num_vowels = 0
    letter_appears_twice = False
    prev_char = ''
    for char in string:
        if char in 'aeiou':
            num_vowels += 1
        if prev_char == char:
            letter_appears_twice = True
        prev_char = char

    not_containing_bad_strings = True
    if 'ab' in string or 'cd' in string or 'pq' in string or 'xy' in string:
        not_containing_bad_strings = False
    
    if num_vowels >= 3 and letter_appears_twice and not_containing_bad_strings:
        nice_strings.append(string)

nice_string_count = len(nice_strings)

if args.target_sum != None:
    if int(args.target_sum) == nice_string_count:
        print('Target matches output')
    else:
        print('Output is incorrect')
else:
    print(nice_string_count)