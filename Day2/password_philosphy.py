from collections import Counter

# Part 1

file_input = []
with open('input.txt', 'r') as file:
    file_input = file.read().splitlines()

valid = 0
for password in file_input:
    temp = password.split(':')
    policy = temp[0]
    policy_count = policy.split(' ')[0]
    policy_char = policy.split(' ')[1]
    count = Counter(temp[1])
    lower_value = int(policy_count.split('-')[0])
    upper_value = int(policy_count.split('-')[1])
    if lower_value <= count[policy_char] <= upper_value:
        valid += 1

print(valid)

# Part 2
valid = 0
for password in file_input:
    temp = password.split(':')
    policy = temp[0]
    pass_string = temp[1].strip()
    policy_count = policy.split(' ')[0]
    policy_char = policy.split(' ')[1]
    lower_value = int(policy_count.split('-')[0]) - 1
    upper_value = int(policy_count.split('-')[1]) - 1
    if (pass_string[lower_value] == policy_char and not pass_string[upper_value] == policy_char) or (not pass_string[lower_value] == policy_char and pass_string[upper_value] == policy_char):
        valid += 1

print(valid)