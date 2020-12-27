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

inverse_bag_rels = {} # child bag

for key, value in bag_rels.items():
    for sub_key, item in value.items():
        inverse_bag_rels[sub_key] = item

def find_child_bag(node):
    bag_count = 0
    path = []
    stack = [node]

    while(len(stack) != 0):
        s = stack.pop()
        print(s)
        # check that items are at the end
        if isinstance(s[-1], int) == False and len(s[-1].items()) != 0:
            if s[0] not in path:
                path.append(s[0])
                parent = 1
                if s[0] != child_bag_color:
                    parent = inverse_bag_rels[s[0]]
                sibling_sum = 0
                
                for key, item in s[-1].items():
                    print(item)
                    if isinstance(item, int):
                        sibling_sum += item
                print(sibling_sum)
               bag_count += sibling_sum * parent
           for key, neighbour in bag_rels[s[0]].items():
                if key in bag_rels:
                    child = bag_rels[key]
                    print((key, child))
                    stack.append((key, child))
    return bag_count

for key, value in bag_rels.items():
    if key == child_bag_color:
        path = find_child_bag((key, value))
        print(path)
