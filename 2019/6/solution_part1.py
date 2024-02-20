import argparse



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

    # Planet keys
    # COM: {B}
    # B: {C, G}
    # C: {D}
    # D: {E, I}
    # E: {F, J}
    # G: {H}
    # J: {K}
    # K: {L}

    def fetch_indirect_moons(planet, orbits):
        indirect_moons = set()
        try: 
            moons = orbits[planet]
            indirect_moons.update(moons)
            for moon in moons:
                indirect_moons.update(fetch_indirect_moons(moon, orbits))
        except KeyError:
            # no more indirect orbits
            return indirect_moons
        
        return indirect_moons

    # Update existing orbits with indirect orbits
    for existing_planet, existing_moons in orbits.items():
        indirect_moons = set()
        for moon in existing_moons:
            indirect_moons.update(fetch_indirect_moons(moon, orbits))
        existing_moons.update(indirect_moons)
    
    print(orbits)
    
    # Tally up orbits
    for planet, moons in orbits.items():
        total_orbit_count += len(moons)

    if args.target_output != None:
        if int(args.target_output) == total_orbit_count:
            print('Target matches output')
        else:
            print('Output is incorrect')
            print(f'Got: {total_orbit_count}')
    else:
        print(total_orbit_count)

if __name__ == '__main__':
    main()