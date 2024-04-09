import argparse
import pdb
import itertools

def main():
    parser = argparse.ArgumentParser(description="Solution to 2019 Day 5 – Part 2")
    parser.add_argument("-i", "--input-file", help="Path to input file")
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

    highest_output = 0
    phase_setting_sequence = ''

    for combination in itertools.permutations(range(5,10), 5):

        output = 0
        sequence = ''.join(map(str, combination))
        print(f'Sequence: {sequence}')

        halt = False

        halted_amplifiers = set()

        memory_1 = list(initial_memory)
        memory_2 = list(initial_memory)
        memory_3 = list(initial_memory)
        memory_4 = list(initial_memory)
        memory_5 = list(initial_memory)

        while not halt:
            
            for amplifier in range(0,5):

                if amplifier not in halted_amplifiers:

                    print(f'Amplifier {amplifier} run')

                    phase_setting = int(sequence[amplifier])

                    # intcode computer below

                    memory = list()

                    if amplifier == 0:
                        memory = memory_1
                    elif amplifier == 1:
                        memory = memory_2
                    elif amplifier == 2:
                        memory = memory_3
                    elif amplifier == 3:
                        memory = memory_4
                    elif amplifier == 4:
                        memory = memory_5

                    instruction_pointer = 0
                    input_instructions_seen = 0

                    while instruction_pointer < len(memory):
                        op = memory[instruction_pointer]

                        op_code = int(op[-2:])

                        if len(op) < 5:
                            extra_zeros = 5 - len(op)
                            for _ in range(0,extra_zeros):
                                op = '0' + op
                            
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
                            if input_instructions_seen == 0:
                                memory[x] = str(phase_setting)
                                input_instructions_seen += 1 
                            else:
                                memory[x] = str(output)

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
                            print(f'op_code: 4 for {amplifier}')
                            output = x
                            print(output)

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
                            # output += int(memory[0])
                            print(f'op_code: 99 for {amplifier}')
                            halted_amplifiers.add(amplifier)
                            if amplifier == 4:
                                # output = int(memory[0])
                                # print(output)
                                halt = True
                            break
                        else:
                            print('something went wrong (bad opcode)')
                            break
    
        if output > highest_output:
            print('Found higher output')
            highest_output = output
            phase_setting_sequence = sequence

    print(highest_output)
    print(phase_setting_sequence)

if __name__ == '__main__':
    main()