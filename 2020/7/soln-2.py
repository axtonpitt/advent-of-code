import argparse

# input
parser = argparse.ArgumentParser(description="Solution to Day 7")
parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
args = parser.parse_args()

# state
bag_rels = {} # contains [bag: [child bag: count, ...]]
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

# get child bags for bag, if contains no other bags return cumulative value, otherwise traverse down child bags
####
### * -- * -- * -- *
###   -- * -- * -- * 
#          -- * -- *
#          -- * -- *
#               -- *
#               -- * 
#               -- *
#               -- *
#
def find_bag_count(target_color, cum_bags):
    print(cum_bags)
    if target_color in bag_rels.keys():
        child_bags = bag_rels[target_color]
        print(child_bags)
        for key in child_bags.keys():
            value = child_bags[key] 
            cum_bags += value
            for i in range(value):
                sum_value = find_bag_count(key, cum_bags)
                sum_value -= cum_bags
                if type(sum_value) != None:
                    cum_bags += sum_value
        return cum_bags
    else:
        return cum_bags

print(find_bag_count(child_bag_color, 0))
