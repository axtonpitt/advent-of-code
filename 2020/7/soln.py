import argparse

# input
parser = argparse.ArgumentParser(description="Solution to Day 7")
parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
args = parser.parse_args()

# state
bag_rels = {}
child_bag_color = "shiny gold"

with open(args.input_file, mode='r') as reader:
    for i, line_raw in enumerate(reader):
        line = line_raw.replace('\n', '')
        rel_info = line.split(' contain ')
        parent = rel_info[0]
        parent_clean = parent.replace(' bags', '')
        children = rel_info[-1]
        child_bags = {}
        if children != 'no other bags.':
            child_array = children.split(', ')
            for child in child_array:
                child_clean = child.replace('.', '').replace(' bags', '').replace(' bag', '').split(' ')
                child_count = int(child_clean[0])
                child_color = "{} {}".format(child_clean[1], child_clean[2])
                child_bags[child_color] = child_count
        if child_bags != {}:
            bag_rels[parent_clean] = child_bags
    print(bag_rels)

outer_bags = {}

def find_child_bag(node, target_bag):
    # first time for this graph if there is a match with the target
    path = []
    stack = [node[0]]

    while(len(stack) != 0):
        if target_bag in path:
            return path
        s = stack.pop()
        if s not in path:
            path.append(s)
        if s not in bag_rels:
            continue
        for neighbour in bag_rels[s]:
            stack.append(neighbour)
    return path

for key, value in bag_rels.items():
    print(key)
    if key != child_bag_color:
        path = find_child_bag((key, value), child_bag_color)
        print(path)
        if path != None and child_bag_color in path:
            outer_bags[path[0]] = True

print(len(outer_bags.keys()))