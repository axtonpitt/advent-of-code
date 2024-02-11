import argparse
from math import floor
import pdb

def main():
    parser = argparse.ArgumentParser(description="Solution to 2019 Day 5 – Part 1")
    parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
    parser.add_argument("-t", "--target-output", help="Target output")
    parser.add_argument("-n", "--program-input")
    args = parser.parse_args()

    # example
    # 1,9,10,3,2,3,11,0,99,30,40,50

    # positions = indices

    # opcodes
    # 1 = adds eg. 1,4,5,9 -> 1,X,Y,Z -> X (int at index X) + Y (int at index Y) = Z (sum stored at index Z)
    # 2 = multiply eg. 2,4,5,9 -> 2,X,Y,Z -> X (int at index X) * Y (int at index Y) = Z (multiple stored at index Z)
    # 3 = moves parameter to specified location e.g. 3,X -> takes input and saves it to address X
    # 4 = outputs the value at address e.g. 4,X -> outputs value at X 
    # 5 = jump-if-true – if first parameter is non-zero, sets instruction pointer to the value from the second parameter
    # 6 = jump-if-false - if the first parameter is zero, sets the pointer to the value from the second parameter
    # 7 = less than – if the first parameter is less than the second parameter it stores 1 in the the position given by the third parameter, otherwise it stores 0
    # 8 = equals – if the first parameter is equal to the second parameter it stores 1 in the position given by the third parameter. Otherwise it stores 0
    # 99 = halt
    # anything else = something went wrong

    initial_memory = []

    with open(args.input_file, mode="r") as reader:
        for line in reader:
            program_str = line.split(',')
            for op_str in program_str:
                initial_memory.append(op_str)

    output = 0

    memory = list(initial_memory)

    instruction_pointer = 0
    while instruction_pointer < len(memory):
        op = memory[instruction_pointer]

        op_code = int(op[-2:])

        if len(op) < 5:
            extra_zeros = 5 - len(op)
            for _ in range(0,extra_zeros):
                op = '0' + op
            
        # TODO: extract mode setting from op_codes

        if op_code == 1 or op_code == 2:
            x_mode = 'position'
            y_mode = 'position'
            z_mode = 'position'

            if int(op[2]) == 1:
                x_mode = 'immediate'
            if int(op[1]) == 1:
                y_mode = 'immediate'

            if x_mode == 'immediate':
                x = memory[instruction_pointer+1]
            else:
                x = memory[int(memory[instruction_pointer+1])]
            x = int(x)

            if y_mode == 'immediate':
                y = memory[instruction_pointer+2]
            else:
                y = memory[int(memory[instruction_pointer+2])]
            y = int(y)

            if z_mode == 'position':
                z = int(memory[instruction_pointer+3])
            z = int(z)

            if op_code == 1:
                memory[z] = str(x + y)
            elif op_code == 2:
                memory[z] = str(x * y)

            instruction_pointer += 4
        
        elif op_code == 3:
            x = int(memory[instruction_pointer+1])
            memory[x] = str(args.program_input)

            instruction_pointer += 2

        elif op_code == 4:
            x_mode = 'position'
            if int(op[2]) == 1:
                x_mode = 'immediate'
            
            if x_mode == 'immediate':
                x = memory[instruction_pointer+1]
            else:
                x = memory[int(memory[instruction_pointer+1])]
            x = int(x)
            print(x)

            instruction_pointer += 2
        
        elif op_code == 5:
            x_mode = 'position'
            y_mode = 'position' 

            if int(op[2]) == 1:
                x_mode = 'immediate'
            if int(op[1]) == 1:
                y_mode = 'immediate'

            if x_mode == 'immediate':
                x = memory[instruction_pointer+1]
            else:
                x = memory[int(memory[instruction_pointer+1])]
            x = int(x)

            if y_mode == 'immediate':
                y = memory[instruction_pointer+2]
            else:
                y = memory[int(memory[instruction_pointer+2])]
            y = int(y)

            if x != 0:
                instruction_pointer = y
            else:
                instruction_pointer += 3

        elif op_code == 6:
            x_mode = 'position'
            y_mode = 'position' 

            if int(op[2]) == 1:
                x_mode = 'immediate'
            if int(op[1]) == 1:
                y_mode = 'immediate'

            if x_mode == 'immediate':
                x = memory[instruction_pointer+1]
            else:
                x = memory[int(memory[instruction_pointer+1])]
            x = int(x)

            if y_mode == 'immediate':
                y = memory[instruction_pointer+2]
            else:
                y = memory[int(memory[instruction_pointer+2])]
            y = int(y)

            if x == 0:
                instruction_pointer = y
            else:
                instruction_pointer += 3

        elif op_code == 7:
            x_mode = 'position'
            y_mode = 'position'
            z_mode = 'position'

            if int(op[2]) == 1:
                x_mode = 'immediate'
            if int(op[1]) == 1:
                y_mode = 'immediate'
            if int(op[0]) == 1:
                z_mode = 'immediate'

            if x_mode == 'immediate':
                x = memory[instruction_pointer+1]
            else:
                x = memory[int(memory[instruction_pointer+1])]
            x = int(x)

            if y_mode == 'immediate':
                y = memory[instruction_pointer+2]
            else:
                y = memory[int(memory[instruction_pointer+2])]
            y = int(y)

            if z_mode == 'immediate':
                z = memory[instruction_pointer+3]
            else:
                z = int(memory[instruction_pointer+3])
            z = int(z)
        
            if x < y:
                memory[z] = 1
            else:
                memory[z] = 0
            instruction_pointer += 4

        elif op_code == 8:
            x_mode = 'position'
            y_mode = 'position'
            z_mode = 'position'

            if int(op[2]) == 1:
                x_mode = 'immediate'
            if int(op[1]) == 1:
                y_mode = 'immediate'
            if int(op[0]) == 1:
                z_mode = 'immediate'

            if x_mode == 'immediate':
                x = memory[instruction_pointer+1]
            else:
                x = memory[int(memory[instruction_pointer+1])]
            x = int(x)

            if y_mode == 'immediate':
                y = memory[instruction_pointer+2]
            else:
                y = memory[int(memory[instruction_pointer+2])]
            y = int(y)

            if z_mode == 'immediate':
                z = memory[instruction_pointer+3]
            else:
                z = int(memory[instruction_pointer+3])
            z = int(z)
        
            if x == y:
                memory[z] = 1
            else:
                memory[z] = 0
            instruction_pointer += 4

        elif op_code == 99:
            output = memory[0]
            break
        else:
            print('something went wrong (bad opcode)')
            break

if __name__ == '__main__':
    main()