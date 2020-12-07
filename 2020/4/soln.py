import math
import argparse
import re

# input
parser = argparse.ArgumentParser(description="Solution to Day 4")
parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
args = parser.parse_args()

valid_passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
required_passport_fields = valid_passport_fields
required_passport_fields.remove('cid')

# state
valid_passports = []
passport_so_far = {}

def is_passport_valid(passport, valid_field_keys):
    print("Passport: {}".format(passport))
    valid = False
    key_match = list(valid_field_keys)
    for key in passport.keys():
        try:
            key_match.remove(key)
        except:
            print("")
    if len(key_match) == 0:
        valid = True
    return valid

with open(args.input_file, mode="r") as reader:                                                                               
    for i, line_raw in enumerate(reader):
        if line_raw != '\n':
            line = line_raw.replace('\n', '')
            fields = line.split(' ')
            for f in fields:
                key_value = f.split(':')
                key = key_value[0]
                value = key_value[-1]
                valid_value = False
                if key == 'byr':
                    if len(value) == 4 and int(value) >= 1920 and int(value) <= 2002:
                        valid_value = True
                if key == 'iyr':
                    if len(value) == 4 and int(value) >= 2010 and int(value) <= 2020:
                        valid_value = True
                if key == 'eyr':
                    if len(value) == 4 and int(value) >= 2020 and int(value) <= 2030:
                        valid_value = True
                if key == 'hgt':
                    reverse = value[::-1]
                    units = reverse[:2]
                    unit = units[::-1]
                    if unit == 'cm':
                        quantity = int(value[:-2])
                        if quantity >= 150 and quantity <= 193:
                            valid_value = True
                    elif unit == 'in':
                        quantity = int(value[:-2])
                        if quantity >= 59 and quantity <= 76:
                            valid_value = True
                if key == 'hcl':
                    p = re.compile(r'#([0-9a-f]){6}')
                    if p.match(value) != None:
                        valid_value = True
                if key == 'ecl':
                    valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                    if value in valid_eye_colors:
                        valid_value = True
                if key == 'pid':
                    if len(value) == 9:
                        valid_value = True
                        
                if valid_value:
                    passport_so_far[key] = value
        else:
            if is_passport_valid(passport_so_far, required_passport_fields):
                valid_passports.append(passport_so_far)
            passport_so_far = {}
    else:
        if is_passport_valid(passport_so_far, required_passport_fields):
            valid_passports.append(passport_so_far)
        passport_so_far = {}

print(len(valid_passports))
