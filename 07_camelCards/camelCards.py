with open('./7_camelCards/example.txt', 'r') as file:
    input = file.readlines()

def main():
    hands = []
    for line in input:
        line = line.split()
        hands.append((line[0], int(line[1])))
    
    sortedHands = selectionSort(hands)
    
    ans = 0
    for i, handBet in enumerate(sortedHands, 1):
        ans += handBet[1] * i
    print(ans)
    
    return


def compareCard(a, b):
    # True means Hand 1 is stronger than hand 2
    cards = 'AKQJT98765432'
    
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
    blocked = ''
    for char in hand:
        if char not in blocked:
            blocked += char
            counts.append(hand.count(char))
            
    
    if max(counts) == 5:
        return 7
    elif max(counts) == 4:
        return 6
    elif max(counts) == 3 and 2 in counts:
        return 5
    elif max(counts) == 3:
        return 4
    elif counts.count(2) == 2:
        return 3
    elif counts.count(2) == 1:
        return 2
    elif counts.count(1) == 5:
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