from os.path import abspath, dirname, join
import re

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().split("\n")

valid_digits = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

def part1(inputs):
    numbers = [re.findall(r"\d", row) for row in inputs]
    ints = [int(number[0]+number[-1] if len(number) > 0 else 0) for number in numbers]
    return sum(ints)

def part2(inputs):
    replacedInput = []
    for row in inputs:
      for key, value in valid_digits.items():
        row = row.replace(key, value)
      replacedInput.append(row)

    return part1(replacedInput)

print(part1(data))
print(part2(data))