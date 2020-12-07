import argparse

# input
parser = argparse.ArgumentParser(description="Solution to Day 6")
parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
args = parser.parse_args()

group_answers = {}
group_members = 0
sum_of_yes = 0

with open(args.input_file, mode='r') as reader:
    for i, line_raw in enumerate(reader):
        if line_raw != '\n':
            line = line_raw.replace('\n', '')
            for char in line:
                print(char)
                if char in group_answers:
                    group_answers[char] += 1
                else:
                    group_answers[char] = 1
            group_members += 1
        else:
            print(group_answers)
            for key, value in group_answers.items():
                if value == group_members:
                    sum_of_yes += 1
            group_answers = {}
            group_members = 0
    else:
        print(group_members)
        for key, value in group_answers.items():
            if value == group_members:
                sum_of_yes += 1 
        group_answers = {}
        group_members = 0

print(sum_of_yes)
