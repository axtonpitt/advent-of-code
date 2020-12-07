import argparse

# input
parser = argparse.ArgumentParser(description="Solution to Day 2")
parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
args = parser.parse_args()

# state
valid_pws = 0

# parse file

with open(args.input_file, mode="r") as reader:
    for line in reader:
        half = line.split(":")
        # 1-2 a: abcdef
        pw = half[-1].replace(" ", "")
        char_rule = half[0].split(" ")
        char_bounds = char_rule[0]
        letter_constraint = char_rule[-1]

        char_rules = char_bounds.split("-")
        char_position_one = int(char_rules[0]) - 1
        char_position_two = int(char_rules[-1]) - 1
        print(char_position_one, char_position_two)

        char_position_one_match = False
        char_position_two_match = False

        try:
            char_one = pw[char_position_one]
            if char_one == letter_constraint:
                char_position_one_match = True
        except:
            print("Invalid index")

        try: 
            char_two = pw[char_position_two]
            if char_two == letter_constraint:
                char_position_two_match = True
        except:
            print("Invalid index 2")

        if char_position_one_match and char_position_two_match:
            print("Both match, therefore invalid password")
        elif char_position_one_match:
            valid_pws += 1
        elif char_position_two_match:
            valid_pws += 1

print(valid_pws)
