import argparse

# input
parser = argparse.ArgumentParser(description="Solution to Day 1")
parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
parser.add_argument("-t", "--target-sum", help="Target sum")
args = parser.parse_args()

# state
expenses = []

with open(args.input_file, mode="r") as reader:
    for line in reader:
        expenses.append(int(line))

soln = 0

for i, expense in enumerate(expenses):
    for j, other_exp in enumerate(expenses):
        for k, yet_exp in enumerate(expenses):
            if i != j and i != k and j != k and expense + other_exp + yet_exp == int(args.target_sum):
                soln = expense * other_exp * yet_exp
                print(soln)
                break
        if soln != 0:
            break
    if soln != 0:
        break