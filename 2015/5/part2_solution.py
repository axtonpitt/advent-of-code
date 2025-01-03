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
    two_letter_combos = []
    contains_two_letter_repeat = False

    three_letter_combos = []
    contains_two_letter_repeat_with_gap = False

    for i in range(0, len(string)):
        if (i - 1) >= 0:
            two_char = string[i-1:i]
            two_letter_combos.append(two_char)

            prev_two_char_array_index = i - 2

            if two_letter_combos.get(prev_two_char_array_index, ''):


        if (i - 2) >= 0:
            three_char = string[i-2:i]
            three_letter_combos.append(three_char)

            prev_three_char_array_index = i - 3

    
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