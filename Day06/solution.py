from functools import reduce
import operator
from os.path import abspath, dirname, join
import re

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().split("\n")

def getWinsInRage(time, record):
    wins = {}
    for i in range(time+1):
      traveled = i * (time - i)
      if traveled > record:
          wins[i] = traveled

    return len(wins)

def part1(inputs):
    inputs = [re.findall(r"\d+", row) for row in inputs]
    numberOfWinsPerRound = []

    for race in range(len(inputs[0])):
        time, record = int(inputs[0][race]), int(inputs[1][race])
        winlen = getWinsInRage(time, record)
        if winlen > 0:
            numberOfWinsPerRound.append(winlen)

    return reduce(operator.mul, numberOfWinsPerRound, 1)

def part2(inputs):
    inputs = [re.findall(r"\d+", row) for row in inputs]
    time = ''.join(inputs[0])
    record = ''.join(inputs[1])
    return getWinsInRage(int(time), int(record))

print(part1(data))
print(part2(data))