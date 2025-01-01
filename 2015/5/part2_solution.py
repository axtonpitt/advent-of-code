import argparse
import hashlib

parser = argparse.ArgumentParser(description="Solution to 2015 Day 5 – Part 2")
parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
parser.add_argument("-t", "--target-sum", help="Target sum")
args = parser.parse_args()

strings = []

with open(args.input_file, mode="r") as reader:
    for line in reader:
        strings.append(line.rstrip())

nice_strings = []

for string in strings:
    prev_char = ''
    prev_prev_char = ''
    two_letter_combos = []
    contains_two_letter_repeat = False

    three_letter_combos = []
    contains_two_letter_repeat_with_gap = False

    for i in range(0, len(string)):
        char = string[i]
        if prev_char != '':
            two_letter_key = f'{prev_char}{char}'
            two_letter_pairs[two_letter_key] = two_letter_pairs.get(two_letter_key, 0) + 1

        if prev_prev_char != '' and prev_char != '':
            if prev_prev_char == char:
                contains_letter_repeat = True

        prev_prev_char = prev_char
        prev_char = char
    
    for pair, freq in two_letter_pairs.items():
        if freq > 1:
            two_letter_pairs_repeats[pair] = freq 
        
    if len(two_letter_pairs_repeats) > 0 and contains_letter_repeat == True:
        nice_strings.append(string)

nice_string_count = len(nice_strings)

if args.target_sum != None:
    if int(args.target_sum) == nice_string_count:
        print('Target matches output')
    else:
        print('Output is incorrect')
else:
    print(nice_string_count)