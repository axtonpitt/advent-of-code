import argparse

parser = argparse.ArgumentParser(description="Solution to day 5")
parser.add_argument("-i", "--input-file", help="Path to input file (with \n seperated data)")
args = parser.parse_args()

# state
total_rows = 128
total_columns = 8

row = 0 
column = 0
row_multiplier = 8
seat_id = 0

curr_row_range = range(total_rows)
curr_col_range = range(total_columns)

seat_ids = {}

with open(args.input_file, mode="r") as reader:
    for i, line_raw in enumerate(reader):
        line = line_raw.replace('\n', '')
        row_instructions = line[:7]
        column_instructions = line[7:]

        for r, inst in enumerate(row_instructions):
            middle_index = len(curr_row_range)//2
            if inst == "F":
                curr_row_range = curr_row_range[:middle_index]
            elif inst == "B":
                curr_row_range = curr_row_range[middle_index:len(curr_row_range)]
            if r == (len(row_instructions) - 1):
                row = list(curr_row_range)[0]

        for c, inst in enumerate(column_instructions):
            middle_index = len(curr_col_range)//2
            if inst == "L":
                curr_col_range = curr_col_range[:middle_index]
            elif inst == "R":
                curr_col_range = curr_col_range[middle_index:len(curr_col_range)]
            if c == (len(column_instructions) - 1):
                column = list(curr_col_range)[0]

        curr_seat_id = (row * row_multiplier) + column
        seat_ids[curr_seat_id] = True

        column = 0
        row = 0
        curr_row_range = range(total_rows)
        curr_col_range = range(total_columns)

previous_seat_id = None
sorted_seat_ids = sorted(seat_ids.keys())
print(sorted_seat_ids)
for seat in sorted_seat_ids:
    print("previous: {}, next: {}".format(previous_seat_id, seat))
    if previous_seat_id != None:
        if (previous_seat_id + 1) != seat:
            print("Found missing seat: {}".format(previous_seat_id + 1))
            seat_id = previous_seat_id + 1
    previous_seat_id = seat

print(seat_id)
