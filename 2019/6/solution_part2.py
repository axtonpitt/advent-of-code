import argparse

class Tree:
    def __init__(self, root_key):
        self.root_key = root_key
        self.up_tree = {}
        self.down_tree = {}

    def add_node(self, node, roots, leaves):
        self.up_tree[node] = roots
        self.down_tree[node] = leaves

def main():
    parser = argparse.ArgumentParser(description="Solution to 2019 Day 6 – Part 2")
    parser.add_argument("-i", "--input-file", help="Path to input file")
    parser.add_argument("-t", "--target-output", help="Target output")
    parser.add_argument("-n", "--program-input")
    args = parser.parse_args()

    orbits = {}
    inverse_orbits = {}

    with open(args.input_file, mode="r") as reader:
        for line in reader:
            orbit_line = line.strip('\n')
            components = orbit_line.split(')')
            planet = components[0]
            moon = components[1]
            inverse_orbits[moon] = planet

            try:
                existing_moons = orbits[planet]
                existing_moons.add(moon)
                orbits[planet] = existing_moons
            except KeyError:
                orbits[planet] = {moon}

    orbits_copy = orbits.copy()
    # Add any planets not as keys
    for planet, moons in orbits_copy.items():
        existing_planets = orbits.keys()
        for moon in moons:
            if moon not in existing_planets:
                orbits[moon] = {}

    # Planet keys
    # COM: {B}
    # B: {C, G}
    # C: {D}
    # D: {E, I}
    # E: {F, J}
    # G: {H}
    # J: {K}
    # K: {L}

    # create tree
    tree = Tree('COM')
    for planet, moons in orbits.items():
        root = ''
        if planet != 'COM':
            root = inverse_orbits[planet]
        tree.add_node(planet, roots={root}, leaves=moons)
                
    you = 'YOU'
    santa = 'SAN'

    # root is the node in the tree that is the planet that the moon is orbiting
    # get all roots to COM for you and santa
    # find common root
    # count length of combined common array

    roots_for_you = []
    orbits_for_you = set()
    you_root = you
    while you_root != 'COM':
        new_you_root = next(iter(tree.up_tree[you_root]))
        roots_for_you.append(new_you_root)
        orbits_for_you.add(new_you_root)
        you_root = new_you_root
    roots_for_you.append('COM')
    orbits_for_you.add('COM')

    roots_for_santa = []
    orbits_for_santa = set()
    santa_root = santa
    while santa_root != 'COM':
        new_santa_root = next(iter(tree.up_tree[santa_root]))
        roots_for_santa.append(new_santa_root)
        orbits_for_santa.add(new_santa_root)
        santa_root = new_santa_root
    roots_for_santa.append('COM')
    orbits_for_santa.add('COM')

    common_orbits = orbits_for_santa.intersection(orbits_for_you)
    unique_orbits = []
    for orbit in roots_for_you:
        if orbit not in common_orbits:
            unique_orbits.append(orbit)
    for orbit in roots_for_santa:
        if orbit not in common_orbits:
            unique_orbits.append(orbit)

    minimum_number_of_orbital_transfers = len(unique_orbits)

    if args.target_output != None:
        if int(args.target_output) == minimum_number_of_orbital_transfers:
            print('Target matches output')
        else:
            print('Output is incorrect')
            print(f'Got: {minimum_number_of_orbital_transfers}')
    else:
        print(minimum_number_of_orbital_transfers)

if __name__ == '__main__':
    main()