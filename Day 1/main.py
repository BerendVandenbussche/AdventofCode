def readFile(filename):
    with open(filename) as calories:
        lines = calories.readlines()
        return lines


def sortCaloriesPerElve(file):
    elveArray = []
    currentElveCalories = []
    elveIndex = 0
    for line in file:
        stripped_line = line.strip('\n')
        if stripped_line:
            currentElveCalories.append(int(stripped_line))
        else:
            elveArray.append(
                {'index': elveIndex, 'calories': currentElveCalories})
            currentElveCalories = []
            elveIndex = elveIndex + 1
    return elveArray


def getTotalCaloriesOfElve(elve):
    totalCalories = 0
    for calory in elve['calories']:
        totalCalories = totalCalories + calory
    return totalCalories


def getElveWithMostCalories(elves):
    totalCalories = []
    for elve in elves:
        totalCalories.append(getTotalCaloriesOfElve(elve))
    return max(totalCalories)


file = readFile('calories.txt')
elves = sortCaloriesPerElve(file)
winner = getElveWithMostCalories(elves)
print(winner)
