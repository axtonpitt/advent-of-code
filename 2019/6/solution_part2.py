import argparse

class Tree:
    def __init__(self):
        self.root_key = ''
        self.tree = {}

    def get_root(self):
        return self.tree[self.root_key]

    def get_leaves(self):
        print()

def main():
    parser = argparse.ArgumentParser(description="Solution to 2019 Day 6 – Part 1")
    parser.add_argument("-i", "--input-file", help="Path to input file")
    parser.add_argument("-t", "--target-output", help="Target output")
    parser.add_argument("-n", "--program-input")
    args = parser.parse_args()

    orbits = {}

    total_orbit_count = 0

    with open(args.input_file, mode="r") as reader:
        for line in reader:
            orbit_line = line.strip('\n')
            components = orbit_line.split(')')
            planet = components[0]
            moon = components[1]

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
                
    distance_to_center = {}

    # Calculate distance of planet to the COM

    def find_com_distance(original_planet, new_planet, distance):
        for other_planet, moons in orbits.items():
            if new_planet in moons:
                if other_planet != 'COM':
                    distance = find_com_distance(original_planet, other_planet, distance)
                    distance += 1
                else:
                    distance += 1
        return distance

    for key in orbits.keys():
        distance = find_com_distance(key, key, 0)
        distance_to_center[key] = distance - 1

    total_orbits = 0

    for planet, moons in orbits.items():
        total_orbits += len(moons)
        if planet != 'COM':
            total_orbits += distance_to_center[planet]

    if args.target_output != None:
        if int(args.target_output) == total_orbits:
            print('Target matches output')
        else:
            print('Output is incorrect')
            print(f'Got: {total_orbits}')
    else:
        print(total_orbits)

if __name__ == '__main__':
    main()