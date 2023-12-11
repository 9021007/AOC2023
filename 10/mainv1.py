input = open("input.txt", "r").read().split("\n")
# input = open("exampleinput.txt", "r").read().split("\n")


# This is the first of two part 2 scripts, use mainv2dec.py for the second part

# This is also the worst code I have ever written.
# Disregard the previous time I said that in AOC2023, this is for real
# 











for i in range(len(input)):
    input[i] = list(input[i])

print(input)

globalsteps = []

for i in range(len(input)):
    globalsteps.append([])
    for j in range(len(input[i])):
        globalsteps[i].append(999999)

        



def findNextTile(x, y, lastx, lasty):
    print(input[y][x])
    if input[y][x] == "|":
        if y+1 != lasty:
            return x, y+1, x, y
        else:
            return x, y-1, x, y
    elif input[y][x] == "-":
        if x+1 != lastx:
            return x+1, y, x, y
        else:
            return x-1, y, x, y
    elif input[y][x] == "L":
        if lastx != x+1:
            return x+1, y, x, y
        else:
            return x, y-1, x, y
    elif input[y][x] == "J":
        if lastx != x-1:
            return x-1, y, x, y
        else:
            return x, y-1, x, y
    elif input[y][x] == "7":
        if lastx != x-1:
            return x-1, y, x, y
        else:
            return x, y+1, x, y
    elif input[y][x] == "F":
        if lastx != x+1:
            return x+1, y, x, y
        else:
            return x, y+1, x, y

animalx = 0
animaly = 0

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "S":
            animalx = j
            animaly = i



def runPipe(stx, sty):
    lastx = animalx
    lasty = animaly
    x = stx
    y = sty
    steps = 0

    inPipe = True
    while inPipe:
        if input[y][x] == "S":
            inPipe = False
            print("FOUND ANIMAL")
            break
        steps += 1
        # print("steps: ", steps)
        # print(x, y)

        if steps < globalsteps[y][x]:
            globalsteps[y][x] = steps
            print("newhigh: ", globalsteps[y][x], " at ", x, y)

        x, y, lastx, lasty = findNextTile(x, y, lastx, lasty)
        # print(x, y)
        
    #while true
        #check if pipe is animal, if so, break
        # find next valid tile from last tile
        # mark number of steps, only if number of steps less than already on tile

# for 4 directions adjacent to animal
# if input[animaly+1][animalx] == "|" or input[animaly+1][animalx] == "L" or input[animaly+1][animalx] == "J" or input[animaly-1][animalx] == "|" or input[animaly-1][animalx] == "7" or input[animaly-1][animalx] == "F" or input[animaly][animalx+1] == "-" or input[animaly][animalx+1] == "J" or input[animaly][animalx+1] == "7" or input[animaly][animalx-1] == "-" or input[animaly][animalx-1] == "L" or input[animaly][animalx-1] == "F":
#     runPipe(animalx, animaly-1)
# split above into 4 if statements
if input[animaly+1][animalx] == "|" or input[animaly+1][animalx] == "L" or input[animaly+1][animalx] == "J":
    runPipe(animalx, animaly+1)
if input[animaly-1][animalx] == "|" or input[animaly-1][animalx] == "7" or input[animaly-1][animalx] == "F":
    runPipe(animalx, animaly-1)
if input[animaly][animalx+1] == "-" or input[animaly][animalx+1] == "J" or input[animaly][animalx+1] == "7":
    runPipe(animalx+1, animaly)
if input[animaly][animalx-1] == "-" or input[animaly][animalx-1] == "L" or input[animaly][animalx-1] == "F":
    runPipe(animalx-1, animaly)

highest = 0
for i in range(len(globalsteps)):
    for j in range(len(globalsteps[i])):
        if globalsteps[i][j] > highest and globalsteps[i][j] != 999999:
            highest = globalsteps[i][j]
print(highest)