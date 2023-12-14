with open('./7_camelCards/input.txt', 'r') as file:
    input = file.readlines()

def main():
    hands = []
    for line in input:
        line = line.split()
        hands.append((line[0], int(line[1])))
    
    sortedHands = selectionSort(hands)
    # print(sortedHands)
    
    ans = 0
    for i, handBet in enumerate(sortedHands, 1):
        ans += handBet[1] * i
    print(ans)
    
    return


def compareCard(a, b):
    # True means Hand 1 is stronger than hand 2
    cards = 'AKQT98765432J'
    
    if getHand(a) == getHand(b):
        # Check for every char
        for i, char in enumerate(a):
            if char != b[i]:
                if cards.find(char) < cards.find(b[i]):
                    return True
                else: 
                    return False
    else:
        if getHand(a) > getHand(b):
            return True
        else: 
            return False
         
        
def getHand(hand):
    counts = []
    blocked = 'J'
    for char in hand:
        if char not in blocked:
            blocked += char
            counts.append(hand.count(char))
    
    if counts == []:
        counts.append(0)
    
    amounts = sorted(counts)
    
    jokers = hand.count("J")
        
    amounts = sorted(counts)
    if jokers >= 5 or amounts[-1] + jokers >= 5:
        return 7
    if jokers >= 4 or amounts[-1] + jokers >= 4:
        return 6

    # Try a full house
    if amounts[-1] + jokers >= 3:
        rem_jokers = amounts[-1] + jokers - 3
        if len(amounts) >= 2 and amounts[-2] + rem_jokers >= 2 or rem_jokers >= 2:
            return 5
        return 4

    if amounts[-1] + jokers >= 2:
        rem_jokers = amounts[-1] + jokers - 2
        if len(amounts) >= 2 and amounts[-2] + rem_jokers >= 2 or rem_jokers >= 2:
            return 3
        return 2

    return 1

def selectionSort(hands):
    for i in range(len(hands)):
        min_index = i
        for j in range(i+1, len(hands)):
            if not compareCard(hands[j][0], hands[min_index][0]):
                min_index = j
        hands[i], hands[min_index] = hands[min_index], hands[i]

    return hands


main()