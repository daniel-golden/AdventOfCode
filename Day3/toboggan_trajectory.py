terrain = []
with open('input.txt', 'r') as file:
    terrain = file.read().splitlines()

position_x = 0
position_y = 0
tree_count = 0
while position_y < len(terrain):
    if terrain[position_y][position_x] == '#':
        tree_count += 1
    position_x = (position_x + 3) % len(terrain[0])
    position_y += 1

print(tree_count)

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
counts = []
for x, y in slopes:
    tree_count = 0
    position_x = 0
    position_y = 0
    while position_y < len(terrain):
        if terrain[position_y][position_x] == '#':
            tree_count += 1
        position_x = (position_x + x) % len(terrain[0])
        position_y += y

    counts.append(tree_count)
total = 1
for count in counts:
    total *= count

print(total)