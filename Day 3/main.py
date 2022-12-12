def readFile(filename):
    with open(filename) as calories:
        lines = calories.readlines()
        return lines


def split_backpacks(lines):
    backpacks = []
    for line in lines:
        line = line.strip('\n')
        half = int((len(line) / 2))
        backpacks.append({'compartment1': line[:half],
                          'compartment2': line[half:]})
    return backpacks


def get_duplicates_from_compartments(backpacks):
    for backpack in backpacks:
        for item in backpack['compartment1']:
            if item in backpack['compartment2']:
                try:
                    if item not in backpack['duplicates']:
                        backpack['duplicates'].append(item)
                except:
                    backpack['duplicates'] = []
                    backpack['duplicates'].append(item)
    return backpacks


def get_points_for_duplicates(backpacks):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for backpack in backpacks:
        try:
            is_upper = backpack['duplicates'][0].isupper()
            index = alphabet.index(backpack['duplicates'][0].lower())+1
            if is_upper:
                index = index+26
            backpack['points'] = index

        except Exception as e:
            pass
    return backpacks


def calculate_total_points(backpacks):
    points = []
    total_points = 0
    for backpack in backpacks:
        try:
            points.append(backpack['points'])
        except Exception as e:
            pass
    for point in points:
        total_points = total_points + point
    return total_points


file = readFile('input.txt')
backpacks = split_backpacks(file)
backpacks_with_duplicates = get_duplicates_from_compartments(backpacks)
points = get_points_for_duplicates(backpacks_with_duplicates)
print(points)
print(calculate_total_points(points))
