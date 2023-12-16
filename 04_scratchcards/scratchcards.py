with open('./4_scratchcards/input.txt', 'r') as file:
    input = file.readlines()

def main():
    ans = 0
    for i in range(len(input)):
        count = 0
        input[i] = input[i].removeprefix(f"Card {i+1}: ").strip("\n").split(" | ")
        input[i][0] = input[i][0].split(" ")
        input[i][1] = input[i][1].split(" ")
        
        for j in range(len(input[i][0])):
            if input[i][0][j] == "" or input[i][0][j] == " ":
                continue
            if input[i][0][j] in input[i][1]:
                count += 1
        
        # print(count)
        if count != 0:
            ans += pow(2, count - 1)
        
    print(ans)
    return

main()
