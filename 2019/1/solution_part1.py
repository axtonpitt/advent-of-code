import argparse
from math import floor

parser = argparse.ArgumentParser(description="Solution to 2019 Day 1 – Part 1")
parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
parser.add_argument("-t", "--target-sum", help="Target sum")
args = parser.parse_args()

def fuel_required_for_mass(mass=int):
    return floor(mass/3) - 2

module_masses = []

with open(args.input_file, mode="r") as reader:
    for line in reader:
        module_masses.append(int(line))

total_required_fuel = 0

for mass in module_masses:
    fuel = fuel_required_for_mass(mass=mass)
    total_required_fuel += fuel

if args.target_sum != None:
    if int(args.target_sum) == total_required_fuel:
        print('Target matches output')
    else:
        print('Output is incorrect')
else:
    print(total_required_fuel)
