import argparse
from math import floor

parser = argparse.ArgumentParser(description="Solution to 2015 Day 2 – Part 2")
parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
parser.add_argument("-t", "--target-sum", help="Target sum")
args = parser.parse_args()

box_dimensions = []

with open(args.input_file, mode="r") as reader:
    for line in reader:
        box_dimensions.append(line)

total_length_ribbon = 0

for dimension in box_dimensions:
    lwh = dimension.split('x')
    l = int(lwh[0])
    w = int(lwh[1])
    h = int(lwh[2])

    # calculate all perimeters of sides
    lw_side = 2*l + 2*w
    wh_side = 2*w + 2*h
    hl_side = 2*h + 2*l

    smallest_side_perimeter = min(lw_side,wh_side,hl_side)    

    volume = l*w*h

    total_length_ribbon += smallest_side_perimeter + volume

if args.target_sum != None:
    if int(args.target_sum) == total_length_ribbon:
        print('Target matches output')
    else:
        print('Output is incorrect')
else:
    print(total_length_ribbon)