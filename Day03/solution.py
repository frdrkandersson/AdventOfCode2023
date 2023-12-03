from collections import defaultdict
from functools import reduce
import operator
from os.path import abspath, dirname, join
import re

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().splitlines()

def mapEngine(schemantic):
    numbers = defaultdict(list)
    symbols = defaultdict(list)
    gears = defaultdict(list)

    for y, row in enumerate(schemantic):
        for number in re.finditer(r"\d+", row):
            numberRange = range(number.start(), number.end())
            numbers[y].append((set(numberRange), int(number.group())))

        for symbol in re.finditer("[^A-Za-z 0-9.]", row):
            scanRange = range(symbol.start()-1, symbol.end()+1)
            symbols[y].append(set(scanRange))

        for gear in re.finditer("\*", row):
            scanRange = range(gear.start()-1, gear.end()+1)
            gears[y].append(set(scanRange))

    return numbers, symbols, gears

def part1(numberDict, symbolDict):
    sum = 0
    for y, symbols in symbolDict.items():
        numbersToScan = numberDict[y-1] + numberDict[y] + numberDict[y+1]
        for symbol in symbols:
            for number in numbersToScan:
                if number[0] & symbol:
                    sum += number[1]
    return sum

def part2(numberDict, gearDict):
    sum = 0
    for y, gears in gearDict.items():
        numbersToScan = numberDict[y-1] + numberDict[y] + numberDict[y+1]
        for gear in gears:
            matchingBuffer = []
            for number in numbersToScan:
                if number[0] & gear:
                    matchingBuffer.append(number[1])

            if len(matchingBuffer) == 2:
                sum += reduce(operator.mul, matchingBuffer, 1)
    return sum

numbers, symbols, gears = mapEngine(data)
print(part1(numbers, symbols))
print(part2(numbers, gears))