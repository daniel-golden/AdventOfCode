expense_entries = []
with open('input.txt', 'r') as file:
    expense_entries = file.read().splitlines()

expense_entries = [int(x) for x in expense_entries]

expense_entries.sort()

start = 0
end = len(expense_entries) - 1

while start < end:
    value = expense_entries[start] + expense_entries[end]
    if value == 2020:
        print(expense_entries[start], expense_entries[end])
        print(expense_entries[start] * expense_entries[end])
        break
    elif value > 2020:
        end -= 1
    else:
        start += 1

check_value = 0
found = False
while check_value < len(expense_entries) and not found:
    start = 0
    end = len(expense_entries) - 1
    comparision = 2020 - expense_entries[check_value]
    while start < check_value and check_value < end:
        value = expense_entries[start] + expense_entries[end]
        if value == comparision:
            print(expense_entries[start], expense_entries[check_value], expense_entries[end])
            print(expense_entries[start] * expense_entries[check_value] * expense_entries[end])
            found = True
            break
        elif value > comparision:
            end -= 1
        else:
            start += 1
    check_value += 1