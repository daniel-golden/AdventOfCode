boarding_passes = []
with open('input.txt', 'r') as file:
    boarding_passes = file.read().splitlines()

max_board = 0
seat_ids = []
for boarding_pass in boarding_passes:
    first_part = boarding_pass[:7]
    second_part = boarding_pass[7:]

    upper_half = 127
    lower_half = 0
    for letter in first_part:
        value = (lower_half + upper_half) // 2
        if letter == 'F':
            upper_half = value
        if letter == 'B':
            lower_half = value + 1

    left_column = 0
    right_column = 7
    for letter in second_part:
        value = (left_column + right_column) // 2
        if letter == 'L':
            right_column = value
        if letter == 'R':
            left_column = value + 1

    boarding_pass_value = upper_half * 8 + left_column
    max_board = max(max_board, boarding_pass_value)
    seat_ids.append(boarding_pass_value)

print(max_board)

seat_ids.sort()
print(seat_ids)
starting_value = seat_ids[1]
for i in range(1, len(seat_ids) - 1):
    if not starting_value == seat_ids[i]:
        print(starting_value)
        starting_value += 1
    starting_value += 1