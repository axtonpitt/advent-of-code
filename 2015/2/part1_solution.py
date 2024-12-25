import argparse
from math import floor

parser = argparse.ArgumentParser(description="Solution to 2015 Day 2 – Part 1")
parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
parser.add_argument("-t", "--target-sum", help="Target sum")
args = parser.parse_args()

box_dimensions = []

with open(args.input_file, mode="r") as reader:
    for line in reader:
        box_dimensions.append(line)

total_surface_area = 0

for dimension in box_dimensions:
    lwh = dimension.split('x')
    l = int(lwh[0])
    w = int(lwh[1])
    h = int(lwh[2])

    lw = l*w
    wh = w*h
    hl = h*l

    smallest_side_area = min(lw,wh,hl)    

    area_of_box = 2*lw + 2*wh + 2*hl

    total_surface_area += (area_of_box + smallest_side_area)

if args.target_sum != None:
    if int(args.target_sum) == total_surface_area:
        print('Target matches output')
    else:
        print('Output is incorrect')
else:
    print(total_surface_area)