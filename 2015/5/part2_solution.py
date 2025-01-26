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

def get_value_or_default(lst, index, default):
    try:
        return lst[index]
    except IndexError:
        return default

for string in strings:
    two_letter_combos_by_index = {}
    contains_two_letter_repeat = False
    
    # iterate through two letter combos
    for i in range(len(string)):
        # look at each pair, the first repeat found much check the index of the previous pair and that it doesn't overlap
        if i > 0:
            two_char = string[i-1:i+1]

            existing_repeats = two_letter_combos_by_index.get(two_char, [])
            existing_repeats.append(i)

            two_letter_combos_by_index[two_char] = existing_repeats

            other_repeats = two_letter_combos_by_index.get(two_char, [])

            # check if any pair is > 2 index apart
            for i in range(len(other_repeats)):
                index = other_repeats[i]
                for j in range(i+1, len(other_repeats)):
                    other_index = other_repeats[j]
                    if other_index - index >= 2:
                        contains_two_letter_repeat = True
                        break
                if contains_two_letter_repeat:
                    break

    contains_two_letter_repeat_with_gap = False

    # iterate through three letter combos
    for i in range(len(string)):
        if i > 2:
            three_char = string[i-2:i+1]

            if three_char[0] == three_char[2]:
                contains_two_letter_repeat_with_gap = True
                break
        
    if contains_two_letter_repeat == True and contains_two_letter_repeat_with_gap == True:
        nice_strings.append(string)

nice_string_count = len(nice_strings)

if args.target_sum != None:
    if int(args.target_sum) == nice_string_count:
        print('Target matches output')
    else:
        print('Output is incorrect')
else:
    print(nice_string_count)