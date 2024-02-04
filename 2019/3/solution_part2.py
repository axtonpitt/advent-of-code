import argparse

def coordinates_for_movements(movements=[]):
    last_coordinate = (0,0)
    last_distance = 0
    coordinate_dict = {}
    for move in movements:
        direction = move[0]
        distance = int(move[1:])

        for step in range(0, distance):
            if direction == "U":
                coordinate = (last_coordinate[0], last_coordinate[1] + 1)
            elif direction == "D":
                coordinate = (last_coordinate[0], last_coordinate[1] - 1)
            elif direction == "L":
                coordinate = (last_coordinate[0] - 1, last_coordinate[1])
            elif direction == "R":
                coordinate = (last_coordinate[0] + 1, last_coordinate[1])

            distance = last_distance + 1
            coordinate_dict[coordinate] = distance
            last_coordinate = coordinate
            last_distance = distance

    return coordinate_dict

def main():
    parser = argparse.ArgumentParser(description="Solution to 2019 Day 3 – Part 1")
    parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
    parser.add_argument("-t", "--target-output", help="Target output")
    args = parser.parse_args()

    paths = []

    with open(args.input_file, mode="r") as reader:
        for line in reader:
            wire_path = line.replace('\n', '').split(',')
            paths.append(wire_path)
    
    path1 = paths[0]
    path2 = paths[-1]

    wire1_coordinates_dict = coordinates_for_movements(movements=path1)
    wire1_coordinates_set = set(wire1_coordinates_dict.keys())
    wire2_coordinates_dict = coordinates_for_movements(movements=path2)
    wire2_coordinates_set = set(wire2_coordinates_dict.keys())

    closest_steps = 1000000000

    intersections = wire1_coordinates_set.intersection(wire2_coordinates_set)

    for intersection in intersections:
        steps = wire1_coordinates_dict[intersection] + wire2_coordinates_dict[intersection]
        if steps < closest_steps and intersection != (0,0):
            closest_steps = steps

    if args.target_output != None:
        if int(args.target_output) == closest_steps:
            print('Target matches output')
        else:
            print('Output is incorrect')
            print(f'Got: {closest_steps}')
    else:
        print(closest_steps)

if __name__ == '__main__':
    main()