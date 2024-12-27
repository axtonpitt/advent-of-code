import argparse
import hashlib

parser = argparse.ArgumentParser(description="Solution to 2015 Day 4 – Part 2")
parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
parser.add_argument("-t", "--target-sum", help="Target sum")
args = parser.parse_args()

secret_key = ''

with open(args.input_file, mode="r") as reader:
    for line in reader:
        secret_key = line

hash_increment = 10000000000000
hash_input = 0

for i in range(0, hash_increment):
    hash_input += 1
    m = hashlib.md5()
    m.update(secret_key.encode())
    m.update(str(hash_input).encode())
    result = m.hexdigest()
    if result[:6] == "000000":
        print(result)
        break

if args.target_sum != None:
    if int(args.target_sum) == hash_input:
        print('Target matches output')
    else:
        print('Output is incorrect')
else:
    print(hash_input)