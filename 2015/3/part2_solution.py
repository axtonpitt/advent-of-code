import argparse
from math import floor

parser = argparse.ArgumentParser(description="Solution to 2015 Day 3 – Part 2")
parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
parser.add_argument("-t", "--target-sum", help="Target sum")
args = parser.parse_args()

directions = []

with open(args.input_file, mode="r") as reader:
    for line in reader:
        for char in line:
            directions.append(char)

coordinates_traversed = {}

def record_coordinates(position_x, position_y, coordinates_traversed):
    coordinate_key = f"{position_x},{position_y}"
    coordinates_traversed[coordinate_key] = coordinates_traversed.get(coordinate_key, 0) + 1

santa_position_x = 0
santa_position_y = 0
robosanta_position_x = 0
robosanta_position_y = 0

record_coordinates(santa_position_x, santa_position_y, coordinates_traversed)
record_coordinates(robosanta_position_x, robosanta_position_y, coordinates_traversed)

for i in range(0, len(directions)):
    direction = directions[i]

    if i % 2 == 0:
        # even (santa)
        if direction == '>':
            santa_position_x += 1
        elif direction == 'v':
            santa_position_y -= 1
        elif direction == '<':
            santa_position_x -= 1
        elif direction == '^':
            santa_position_y += 1
        
        record_coordinates(santa_position_x, santa_position_y, coordinates_traversed)

    else:
        # odd (robosanta)
        if direction == '>':
            robosanta_position_x += 1
        elif direction == 'v':
            robosanta_position_y -= 1
        elif direction == '<':
            robosanta_position_x -= 1
        elif direction == '^':
            robosanta_position_y += 1
        
        record_coordinates(robosanta_position_x, robosanta_position_y, coordinates_traversed)

houses_receiving_presents = len(coordinates_traversed)

if args.target_sum != None:
    if int(args.target_sum) == houses_receiving_presents:
        print('Target matches output')
    else:
        print('Output is incorrect')
else:
    print(houses_receiving_presents)