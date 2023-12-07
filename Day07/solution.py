from functools import reduce
from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().split("\n")

score = {
    'five-of-a-kind': 7,
    'four-of-a-kind': 6,
    'full-house': 5,
    'three-of-a-kind': 4,
    'two-pair': 3,
    'one-pair': 2,
    'high-card': 1
}

def getRanking(hand, useJoker):    
    charStrength = {}
    if useJoker:     
        charStrength = {
            'A': '15',
            'K': '14',
            'Q': '13',
            'T': '11',
            '9': '10',
            '8': '09',
            '7': '08',
            '6': '07',
            '5': '06',
            '4': '05',
            '3': '04',
            '2': '03',
            '1': '02',
            'J': '01'
        }   
    else:
        charStrength = {
            'A': '15',
            'K': '14',
            'Q': '13',
            'J': '12',
            'T': '11',
            '9': '10',
            '8': '09',
            '7': '08',
            '6': '07',
            '5': '06',
            '4': '05',
            '3': '04',
            '2': '03',
            '1': '02',            
        }
        
    ranking = ''
    for i in range(5):            
        ranking += charStrength[hand[i]]

    return float('0.' + ranking)

def elevate(currentScore, hand):
    count = hand.count('J')
    if count < 1:
        return currentScore

    if currentScore == score['high-card']: # XABCJ
        return score['one-pair']    
    if currentScore == score['four-of-a-kind']: # JJJJB BBBBJ
        return score['five-of-a-kind']
    if currentScore == score['three-of-a-kind']: # JJJXB BBBJX
        return score['four-of-a-kind']
    if currentScore == score['full-house']: #JJXXX
        return score['five-of-a-kind']
    if currentScore == score['one-pair']: #JJXEF
        return score['three-of-a-kind']
    if currentScore == score['two-pair']:
        if count == 1: #XXJFF
            return score['full-house']
        elif count == 2: # JJXFF
            return score['four-of-a-kind']
    
    return currentScore    

def checkGame(inputs, useJoker):
    scores = {}    
    games = {}
    for row in inputs:
        hand, bid = row.split()        
        games[hand] = int(bid)        
    
    for game in games.items():
        sortedHand = sorted(game[0])
        lastTwo = ('', '')                
        currentScore = score['high-card']
        for card in sortedHand:
            if lastTwo[1] == card:
                if currentScore == score['high-card']:
                    currentScore = max(score['one-pair'], currentScore)
                elif currentScore == score['one-pair']:
                    if lastTwo[0] == lastTwo[1]:
                        currentScore = max(score['three-of-a-kind'], currentScore)
                    else:
                        currentScore = max(score['two-pair'], currentScore)
                elif currentScore == score['two-pair']:
                    currentScore = max(score['full-house'], currentScore)
                elif currentScore == score['three-of-a-kind']:
                    if lastTwo[0] == lastTwo[1]:
                        currentScore = max(score['four-of-a-kind'], currentScore)
                    else:
                        currentScore = max(score['full-house'], currentScore)
                elif currentScore == score['four-of-a-kind']:
                    currentScore = max(score['five-of-a-kind'], currentScore)

            lastTwo = (lastTwo[1], card)

        if useJoker:
            currentScore = elevate(currentScore, sortedHand)

        scores[game[0]] = currentScore + getRanking(game[0], useJoker)        

    scores = sorted(scores.items(), key=lambda item: item[1]) #sort by value

    result = 0
    for i in range(len(scores)):
        bid = games[scores[i][0]]
        result += bid * (i + 1)

    return result

def part1(inputs):        
    return checkGame(inputs, False)

def part2(inputs):
    return checkGame(inputs, True)

print(part1(data))
print(part2(data))