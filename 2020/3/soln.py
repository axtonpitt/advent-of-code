import math
import argparse

# input
parser = argparse.ArgumentParser(description="Solution to Day 3")
parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
args = parser.parse_args()

def clamped_x(curr_x, limit):
    overflow_count = math.floor(curr_x / limit)
    clamped_val = curr_x - (limit * overflow_count)
    return clamped_val

def determine_trees(trajectory, tree_char):
    toboggan_trajectory = trajectory
    tree = tree_char
    curr_traversal_x = 0
    traversal_x_overflow = 0
    curr_traversal_y = 0
    trees_encountered = 0

    with open(args.input_file, mode="r") as reader:
        for i, line_raw in enumerate(reader):
            line = line_raw.replace('\n', '')
            if curr_traversal_y % toboggan_trajectory[1] == 0 and curr_traversal_y != 0:
                curr_traversal_x += toboggan_trajectory[0]
                char_at_x = ""
                if curr_traversal_x >= len(line):
                    curr_traversal_x = int(clamped_x(curr_traversal_x, len(line)))

                char_at_x = line[curr_traversal_x]

                if char_at_x == tree:
                    trees_encountered += 1
            curr_traversal_y += 1

    return trees_encountered

traversals = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_counts = [] 
tree = "#"
tree_multiple = 1

for t in traversals:
    count = determine_trees(t, tree)
    tree_counts.append(count)
    tree_multiple *= count

print(tree_multiple)
