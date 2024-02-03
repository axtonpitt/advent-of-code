import argparse

def coordinates_for_movements(movements=[]):
    coordinates = [(0,0)]
    coordinate_set = {(0,0)}
    for move in movements:
        direction = move[0]
        distance = int(move[1:])

        for step in range(0, distance):
            last_coordinate = coordinates[-1]

            if direction == "U":
                coordinate = (last_coordinate[0], last_coordinate[1] + 1)
                coordinates.append(coordinate)
                coordinate_set.add(coordinate)
            elif direction == "D":
                coordinate = (last_coordinate[0], last_coordinate[1] - 1)
                coordinates.append(coordinate)
                coordinate_set.add(coordinate)
            elif direction == "L":
                coordinate = (last_coordinate[0] - 1, last_coordinate[1])
                coordinates.append(coordinate)
                coordinate_set.add(coordinate)
            elif direction == "R":
                coordinate = (last_coordinate[0] + 1, last_coordinate[1])
                coordinates.append(coordinate)
                coordinate_set.add(coordinate)

    return coordinate_set

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

    wire1_coordinates = coordinates_for_movements(movements=path1)
    wire2_coordinates = coordinates_for_movements(movements=path2)

    closest_distance = 1000000000

    intersections = wire1_coordinates.intersection(wire2_coordinates)

    for intersection in intersections:
        distance = abs(intersection[0]) + abs(intersection[1])
        if distance < closest_distance and intersection != (0,0):
            closest_distance = distance

    if args.target_output != None:
        if int(args.target_output) == closest_distance:
            print('Target matches output')
        else:
            print('Output is incorrect')
    else:
        print(closest_distance)

if __name__ == '__main__':
    main()