from collections import defaultdict
from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().splitlines()    

def part1(inputs):
    sum = 0
    for game in inputs:        
        game = game[7:] # Remove Card x: 
        win, played = game.split('|')
        win = set(win.split())
        played = set(played.split())        
        wins = win & played

        score = 0
        for _ in range(len(wins)):
            if score == 0:
                score = 1
            else:
                score *= 2

        sum += score
    
    return sum

def part2(inputs):    
    copies = defaultdict(int)
    for i, game in enumerate(inputs):
        game = game[7:] # Remove Card x: 
        win, played = game.split('|')
        win = set(win.split())
        played = set(played.split())
        wins = win & played
        
        copies[i] += 1
        for j in range(len(wins)):            
            copies[i+j+1] += 1 * copies[i]
    
    return sum(copies.values())

print(part1(data))
print(part2(data))