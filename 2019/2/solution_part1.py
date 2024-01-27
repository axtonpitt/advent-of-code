import argparse
from math import floor
import pdb

def main():
    parser = argparse.ArgumentParser(description="Solution to 2019 Day 2 – Part 1")
    parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
    parser.add_argument("-t", "--target-output", help="Target output")
    args = parser.parse_args()

    # example
    # 1,9,10,3,2,3,11,0,99,30,40,50

    # positions = indices

    # opcodes
    # 1 = adds eg. 1,4,5,9 -> 1,X,Y,Z -> X (int at index X) + Y (int at index Y) = Z (sum stored at index Z)
    # 2 = multiply eg. 1,4,5,9 -> 1,X,Y,Z -> X (int at index X) * Y (int at index Y) = Z (multiple stored at index Z)
    # 99 = halt
    # anything else = something went wrong

    initial_memory = []

    with open(args.input_file, mode="r") as reader:
        for line in reader:
            program_str = line.split(',')
            for op_str in program_str:
                initial_memory.append(int(op_str))

    noun_address = 1
    noun = 12
    verb_address = 2
    verb = 2

    memory = initial_memory

    memory[noun_address] = noun
    memory[verb_address] = verb

    output = 0

    def operation_processor(op_code=int, parameters=[]):
        operation = ''
        if op_code == 1:
            operation = '+'
        elif op_code == 2:
            operation = '*'

        values = []

        for address in parameters:
            value = memory[address]
            values.append(value)
        
        output = 0
        if operation == '+':
            output = values[0] + values[1]
        elif operation == '*':
            output = values[0] * values[1]
        
        return output

    instruction_pointer = 0
    while instruction_pointer < len(memory):
        op = memory[instruction_pointer]
        if op == 1 or op == 2:
            x_address = memory[instruction_pointer+1]
            y_address = memory[instruction_pointer+2]
            z_address = memory[instruction_pointer+3]
            new_value = operation_processor(op_code=op, parameters=[x_address,y_address,z_address])
            memory[z_address] = new_value

        elif op == 99:
            output = memory[0]
            print('program halt')
            break

        else:
            print('something went wrong (bad opcode)')
            break
    
        instruction_pointer += 4

    if args.target_output != None:
        if int(args.target_output) == output:
            print('Target matches output')
        else:
            print(f'output = {output}')
            print('Output is incorrect')
    else:
        print(output)

if __name__ == '__main__':
    main()