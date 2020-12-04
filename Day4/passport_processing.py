passports = []
with open('input.txt', 'r') as file:
    passports = file.read().splitlines()

passports_split = []
values = []
temp = ''
for passport in passports:
    if passport:
        temp += passport + ' '
    else:
        temp = temp[:-1]
        values.append(temp)
        temp = ''
values.append(temp)

for passport in values:
    passport_sorted = {}
    attributes = passport.split(' ')
    for attribute in attributes:
        attr = attribute.split(':')
        if attr[0] and attr[1]:
            passport_sorted[attr[0]] = attr[1]
    if passport_sorted:
        passports_split.append(passport_sorted)

must_have = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid = 0
for passport in passports_split:
    has_all = True
    for attr in must_have:
        if not attr in passport.keys():
            has_all = False
            break
    if has_all:
        valid += 1

print(valid)


# Part 2
def validate_byr(byr):
    if 1920 <= int(byr) <= 2002:
        return True
    return False

def validate_iyr(iyr):
    if 2010 <= int(iyr) <= 2020:
        return True
    return False

def validate_eyr(eyr):
    if 2020 <= int(eyr) <= 2030:
        return True
    return False

def validate_hgt(hgt):
    if 'cm' in hgt:
        hgt_cm = hgt.split('cm')
        if 150 <= int(hgt_cm[0]) <= 193:
            return True
        return False
    if 'in' in hgt:
        hgt_in = hgt.split('in')
        if 59 <= int(hgt_in[0]) <= 76:
            return True
        return False
    return False

def validate_hcl(hcl):
    if '#' == hcl[0] and len(hcl) == 7:
        if hcl[1:].isalnum():
            return True
        return False
    return False

def validate_ecl(ecl):
    must_contain = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl in must_contain:
        return True
    return False

def validate_pid(pid):
    if len(pid) == 9 and pid.isnumeric():
        return True
    return False

must_have = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid = 0
for passport in passports_split:
    has_all = True
    for attr in must_have:
        if not attr in passport.keys():
            has_all = False
            break
        if attr == 'byr':
            if not validate_byr(passport[attr]):
                has_all = False
                break
        if attr == 'iyr':
            if not validate_iyr(passport[attr]):
                has_all = False
                break
        if attr == 'eyr':
            if not validate_eyr(passport[attr]):
                has_all = False
                break
        if attr == 'hgt':
            if not validate_hgt(passport[attr]):
                has_all = False
                break
        if attr == 'ecl':
            if not validate_ecl(passport[attr]):
                has_all = False
                break
        if attr == 'hcl':
            if not validate_hcl(passport[attr]):
                has_all = False
                break
        if attr == 'pid':
            if not validate_pid(passport[attr]):
                has_all = False
                break
    if has_all:
        valid += 1

print(valid)