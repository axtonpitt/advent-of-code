import argparse
import hashlib
import numpy as np

parser = argparse.ArgumentParser(description="Solution to 2015 Day 6 – Part 1")
parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
parser.add_argument("-t", "--target-sum", help="Target sum")
args = parser.parse_args()

instructions = []

with open(args.input_file, mode="r") as reader:
    for line in reader:
        instructions.append(line)

# example instructions; remember the numbers are coordinates x,y from 0-999
# turn off 301,3 through 808,453
# turn on 351,678 through 951,908
# toggle 720,196 through 897,994

lights = np.zeros((1000, 1000), dtype=int)

for instruction in instructions:
    instruction_parts = instruction.split(' through ')
    end_coordinates = instruction_parts[1]
    start_coordinates_and_type = instruction_parts[0]

    end_x = int(end_coordinates.split(',')[0])
    end_y = int(end_coordinates.split(',')[1])

    if 'toggle' in start_coordinates_and_type:
        start_coordinates = start_coordinates_and_type.split(' ')[1]
        start_x = int(start_coordinates.split(',')[0])
        start_y = int(start_coordinates.split(',')[1])
        lights[start_x:end_x+1, start_y:end_y+1] += 2

    else:
        start_coordinates = start_coordinates_and_type.split(' ')[2]
        start_x = int(start_coordinates.split(',')[0])
        start_y = int(start_coordinates.split(',')[1])
        type_of_instruction = start_coordinates_and_type.split(' ')[1]
        if type_of_instruction == 'on':
            lights[start_x:end_x+1, start_y:end_y+1] += 1
        else:
            lights[start_x:end_x+1, start_y:end_y+1] = np.maximum(0, lights[start_x:end_x+1, start_y:end_y+1] - 1)

brightness_value = np.sum(lights)

if args.target_sum != None:
    if int(args.target_sum) == brightness_value:
        print('Target matches output')
    else:
        print('Output is incorrect')
else:
    print(brightness_value)