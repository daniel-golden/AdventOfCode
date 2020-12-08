from collections import defaultdict

input = []
with open('input.txt', 'r') as file:
    input = file.read().splitlines()

bag_dictionary = defaultdict(list)
for bags in input:
    temp = bags.split('contain')
    key = temp[0][:-1].replace(' bags', '').replace(' bag', '')
    value = temp[1].replace('.','').split(',')
    for i in range(len(value)):
        if 'no' in value[i]:
            bag_dictionary[key].append(value[i][1:].replace(' bags', '').replace(' bag', ''))
        else:
            bag_dictionary[key].append(value[i][3:].replace(' bags', '').replace(' bag', ''))

def dfs(bag):
    gold_bag = False
    for x in bag:
        if x == 'shiny gold':
            return True
        elif x == 'no other':
            return False
        else:
            gold_bag = gold_bag or dfs(bag_dictionary[x])
    if gold_bag:
        return 1
    else:
        return 0

count = 0
for key, value in bag_dictionary.copy().items():
    count += dfs(value)

print(count)


#part 2
bag_dictionary = defaultdict(list)
for bags in input:
    temp = bags.split('contain')
    key = temp[0][:-1].replace(' bags', '').replace(' bag', '')
    value = temp[1].replace('.','').split(',')
    for i in range(len(value)):
        if 'no' in value[i]:
            bag_dictionary[key].append([1, value[i][1:].replace(' bags', '').replace(' bag', '')])
        else:
            temp = value[i].split(' ')
            bag_info = [temp[1],value[i][3:].replace(' bags', '').replace(' bag', '')]
            bag_dictionary[key].append(bag_info)


start_bag = bag_dictionary['shiny gold']
equation = []
count = 0
def dfs_count(bag):
    temp = 0
    for x in bag:
        if x[1] == 'no other':
            return 0
        value = int(x[0])
        value2 = value * dfs_count(bag_dictionary[x[1]])
        temp += value + value2

    return temp

cumm = 0
for bag in start_bag:
    value = int(bag[0])
    temp = dfs_count(bag_dictionary[bag[1]])
    cumm += (value + (value * temp))

print(cumm)