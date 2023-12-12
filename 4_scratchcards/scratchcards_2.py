with open('./4_scratchcards/input.txt', 'r') as file:
    input = file.readlines()

def main():
    cardCount = []
    for card in input:
        cardCount.append(1)
        
    for i in range(len(input)):
        cardID = i + 1
        count = (findMatches(input[i], cardID))
        for k in range(cardCount[i]):
            for j in range(cardID + 1, i + count + 2):
                cardCount[j-1] += 1
    print(sum(cardCount))
    return

def findMatches(input, i):
    count = 0
    input = input.removeprefix(f"Card {i}: ").strip("\n").split(" | ")
    input[0] = input[0].split(" ")
    input[1] = input[1].split(" ")
    
    for j in range(len(input[0])):
        if input[0][j] == "" or input[0][j] == " ":
            continue
        if input[0][j] in input[1]:
            count += 1
    
    return count

main()
