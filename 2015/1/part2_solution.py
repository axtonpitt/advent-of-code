import argparse
from math import floor

parser = argparse.ArgumentParser(description="Solution to 2015 Day 1 – Part 2")
parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
parser.add_argument("-t", "--target-sum", help="Target sum")
args = parser.parse_args()

instructions = []

with open(args.input_file, mode="r") as reader:
    for line in reader:
        for char in line:
            instructions.append(char)


santa_floor = 0
index_of_basement = 0

for i in range(len(instructions)):
    instruction = instructions[i]
    if instruction == "(":
        santa_floor += 1
    elif instruction == ")":
        santa_floor -= 1
    if santa_floor == -1:
        index_of_basement = i
        break

position_of_basement_transition = index_of_basement + 1

if args.target_sum != None:
    if int(args.target_sum) == position_of_basement_transition:
        print('Target matches output')
    else:
        print('Output is incorrect')
else:
    print(position_of_basement_transition)