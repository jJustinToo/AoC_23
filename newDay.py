import os

dayInput = input("Day: ")
challengeName = input("Case sensitive.\nChallenge Name: ")

name = f'{dayInput}_{challengeName}'

if name not in os.listdir():
    os.mkdir(name)
    with open(f"./{name}/{challengeName}.py", "w") as file:
        file.write(f"with open('./{name}/input.txt', 'r') as file:\n    input = file.readlines()\n\ndef main():\n    \n    return\n\nmain()")
    open(f"./{name}/{challengeName}_2.py", "w").close()
    open(f"./{name}/input.txt", "w").close()
    open(f"./{name}/example.txt", "w").close()