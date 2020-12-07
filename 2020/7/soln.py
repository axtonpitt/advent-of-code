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
# determine paths to child
paths = {}
tmp_path = []

# invert tree
inverted_bag_rels = {}

for key, value in bag_rels.items():
    for bag in value:
        if bag not in inverted_bag_rels:
            inverted_bag_rels[bag] = [key]
        else:
            existing = inverted_bag_rels[bag]
            existing.append(key)
            inverted_bag_rels[bag] = existing

parents_of_target_child = inverted_bag_rels[child_bag_color]
for parent in parents_of_target_child:
    paths[parent] = True
    if parent in inverted_bag_rels:
        for item in inverted_bag_rels[parent]:
            paths[item] = True

print(len(paths.keys()))

