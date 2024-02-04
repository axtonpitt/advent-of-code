import argparse

def main():
    parser = argparse.ArgumentParser(description="Solution to 2019 Day 3 – Part 1")
    parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
    parser.add_argument("-t", "--target-output", help="Target output")
    args = parser.parse_args()

    password_range = range(0)

    valid_password_count = 0 

    with open(args.input_file, mode="r") as reader:
        for line in reader:
            password_range_arr = line.split('-')
            password_range = range(int(password_range_arr[0]), int(password_range_arr[1])+ 1)
    
    for password_int in password_range:
        password = str(password_int)
        contains_repeat = False
        never_decreases = True

        if len(password) == 6:
            previous_char = -1
            for char in password:
                digit = int(char)
                previous_digit = int(previous_char)

                if digit == previous_digit:
                    contains_repeat = True

                if digit < previous_digit:
                    never_decreases = False

                previous_char = char
            
            if contains_repeat and never_decreases:
                valid_password_count += 1

        else:
            continue

    if args.target_output != None:
        if int(args.target_output) == valid_password_count:
            print('Target matches output')
        else:
            print('Output is incorrect')
            print(f'Got: {valid_password_count}')
    else:
        print(valid_password_count)

if __name__ == '__main__':
    main()