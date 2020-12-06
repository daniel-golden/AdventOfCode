input = []
with open('input.txt', 'r') as file:
    input = file.read().splitlines()

custom_answers = []
temp = ''
for line in input:
    if not line:
        custom_answers.append(temp)
        temp = ''
    else:
        temp += line

if temp:
    custom_answers.append(temp)

count = 0
for answers in custom_answers:
    total_answers = set(answers)
    count += len(total_answers)

print(count)

#part 2
answers = []
temp = []
for line in input:
    if not line:
        answers.append(temp)
        temp = []
    else:
        temp.append(line)

if temp:
    answers.append(temp)

count = 0
for group in answers:
    same = set(group[0])
    for answer in group:
        same = same.intersection(answer)
    count += len(same)

print(count)