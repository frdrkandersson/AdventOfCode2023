from functools import reduce
import operator
from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().split("\n")

sack = { "red": 12, "green": 13, "blue": 14 }

def parseGame(row):
    highestCubeCount = { "red": 0, "green": 0, "blue": 0 }
    row = row[4:] # remove "Game "
    gameId, game = row.split(':')
    sets = game.split(';')
    for set in sets:
        cubes = set.split(',')
        for cube in cubes:
            cubeCount, cubeColor = cube.split()
            highestCubeCount[cubeColor] = max(highestCubeCount[cubeColor], int(cubeCount))
    return gameId, highestCubeCount

def part1(inputs):
    sum = 0
    for game in inputs:
        gameId, cubeCount = parseGame(game)
        validGame = True
        for color, count in sack.items():
          if cubeCount[color] > count:
              validGame = False

        if validGame:
          sum += int(gameId)

    return sum

def part2(inputs):
    sum = 0
    for game in inputs:
        _, cubeCount = parseGame(game)
        sum += reduce(operator.mul, cubeCount.values(), 1)

    return sum

print(part1(data))
print(part2(data))