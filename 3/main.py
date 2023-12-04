import os

input = open("input.txt", "r").read().split("\n")

numbers = []

for i in range(len(input)):
    # print("line " + str(i))
    # (val, line, pos, length)
    
    digitpos = []
    for j in range(len(input[i])):
        if input[i][j] == "0" or input[i][j] == "1" or input[i][j] == "2" or input[i][j] == "3" or input[i][j] == "4" or input[i][j] == "5" or input[i][j] == "6" or input[i][j] == "7" or input[i][j] == "8" or input[i][j] == "9":
            digitpos.append(j)
    # print(digitpos)
    # check if positions are sequential
    for j in range(len(digitpos)):
        if j != len(digitpos)-1:
            # print(1,j, digitpos[j])
            if digitpos[j] == digitpos[j+1] - 1:
                # print("pair located")
                if j != len(digitpos) -2:
                    if digitpos[j] == digitpos[j+2] - 2:
                        # print("triple located")
                        numbers.append((int(str(input[i][digitpos[j]])+str(input[i][digitpos[j+1]])+str(input[i][digitpos[j+2]])), i, digitpos[j], 3))
                    else:
                        numbers.append(((int(str(input[i][digitpos[j]])+str(input[i][digitpos[j+1]])), i, digitpos[j], 2)))
                else:
                    numbers.append((int(str(input[i][digitpos[j]])+str(input[i][digitpos[j+1]])), i, digitpos[j], 2))
            else:
                numbers.append((int(input[i][digitpos[j]]), i, digitpos[j], 1))
        else:
            numbers.append((int(input[i][digitpos[j]]), i, digitpos[j], 1))

donot = []
do = []

for i in range(len(numbers)):
    if numbers[i][3] == 3:
        do.append(numbers[i])
        donot.append(numbers[i+1])
        donot.append(numbers[i+2])
    if numbers[i][3] == 2:
        if numbers[i] not in donot:
            do.append(numbers[i])
            donot.append(numbers[i+1])
    if numbers[i][3] == 1:
        if numbers[i] not in donot:
            do.append(numbers[i])

# print(do)

numbers = do
symbolnumbers = []
symbolpositions = []

for i in range(len(numbers)):
    if numbers[i][2] != 0:
        if input[numbers[i][1]][numbers[i][2]-1] == ".":
            if numbers[i][1] != 0:
                if input[numbers[i][1]-1][numbers[i][2]-1] == ".":
                    # print("upper left")
                    pass
                else:
                    symbolnumbers.append(numbers[i])
                    symbolpositions.append((numbers[i][1]-1, numbers[i][2]-1, numbers[i]))
            if numbers[i][1] != len(input) -1:
                if input[numbers[i][1]+1][numbers[i][2]-1] == ".":
                    # print("lower left")
                    pass
                else:
                    symbolnumbers.append(numbers[i])
                    symbolpositions.append((numbers[i][1]+1, numbers[i][2]-1, numbers[i]))
        else:
            symbolnumbers.append(numbers[i])
            symbolpositions.append((numbers[i][1], numbers[i][2]-1, numbers[i]))
            # print("left only", numbers[i])
    if numbers[i][2]+numbers[i][3] < len(input[numbers[i][1]]) -1:
        if input[numbers[i][1]][numbers[i][2]+numbers[i][3]] == ".":
            if numbers[i][1] != 0:
                if input[numbers[i][1]-1][numbers[i][2]+numbers[i][3]] == ".":
                    # print("upper right")
                    pass
                else:
                    symbolnumbers.append(numbers[i])
                    symbolpositions.append((numbers[i][1]-1, numbers[i][2]+numbers[i][3], numbers[i]))
            if numbers[i][1] != len(input) -1:
                if input[numbers[i][1]+1][numbers[i][2]+numbers[i][3]] == ".":
                    # print("lower right")
                    pass
                else:
                    symbolnumbers.append(numbers[i])
                    symbolpositions.append((numbers[i][1]+1, numbers[i][2]+numbers[i][3], numbers[i]))
        else:
            symbolnumbers.append(numbers[i])
            symbolpositions.append((numbers[i][1], numbers[i][2]+numbers[i][3], numbers[i]))
            # print("right only", numbers[i])
    if numbers[i][1] != 0:
        if numbers[i][3] == 3:
            if input[numbers[i][1]-1][numbers[i][2]:numbers[i][2] + 3] != "...":
                symbolnumbers.append(numbers[i])
                symbolpositions.append((numbers[i][1]-1, numbers[i][2], numbers[i]))
                symbolpositions.append((numbers[i][1]-1, numbers[i][2]+1, numbers[i]))
                symbolpositions.append((numbers[i][1]-1, numbers[i][2]+2, numbers[i]))
                # print("ABOVE 3")
        if numbers[i][3] == 2:
            if input[numbers[i][1]-1][numbers[i][2]:numbers[i][2] + 2] != "..":
                symbolnumbers.append(numbers[i])
                symbolpositions.append((numbers[i][1]-1, numbers[i][2], numbers[i]))
                symbolpositions.append((numbers[i][1]-1, numbers[i][2]+1, numbers[i]))
                # print("ABOVE 2")
        if numbers[i][3] == 1:
            if input[numbers[i][1]-1][numbers[i][2]] != ".":
                symbolnumbers.append(numbers[i])
                symbolpositions.append((numbers[i][1]-1, numbers[i][2], numbers[i]))
                # print("ABOVE 1")
    if numbers[i][1] != len(input) -1:
        if numbers[i][3] == 3:
            if input[numbers[i][1]+1][numbers[i][2]:numbers[i][2] + 3] != "...":
                symbolnumbers.append(numbers[i])
                symbolpositions.append((numbers[i][1]+1, numbers[i][2], numbers[i]))
                symbolpositions.append((numbers[i][1]+1, numbers[i][2]+1, numbers[i]))
                symbolpositions.append((numbers[i][1]+1, numbers[i][2]+2, numbers[i]))
                # print("BELOW 3")
        if numbers[i][3] == 2:
            if input[numbers[i][1]+1][numbers[i][2]:numbers[i][2] + 2] != "..":
                symbolnumbers.append(numbers[i])
                symbolpositions.append((numbers[i][1]+1, numbers[i][2], numbers[i]))
                symbolpositions.append((numbers[i][1]+1, numbers[i][2]+1, numbers[i]))
                # print("BELOW 2")
        if numbers[i][3] == 1:
            if input[numbers[i][1]+1][numbers[i][2]] != ".":
                symbolnumbers.append(numbers[i])
                symbolpositions.append((numbers[i][1]+1, numbers[i][2], numbers[i]))
                # print("BELOW 1")



# print(numbers)
# print(symbolnumbers)

# remove duplicates
symbolnumbers = list(set(symbolnumbers))

# sum all values
sum = 0

for i in range(len(symbolnumbers)):
    sum += symbolnumbers[i][0]

# print(sum)

stars = []

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "*":
            stars.append((i, j))

# print(stars[0])

# print(symbolpositions[0])

gears = []
debugears = []

# find where same stars are have 2 adjacent numbers

for i in range(len(stars)):
    touching = []
    for j in range(len(symbolpositions)):
        if symbolpositions[j][0] == stars[i][0]:
            if symbolpositions[j][1] == stars[i][1]:
                touching.append(symbolpositions[j])
    if len(touching) == 2:
        gears.append(touching[0][2][0]*touching[1][2][0])
        debugears.append((touching[0], touching[1], touching[0][2][0], touching[1][2][0], touching[0][2][0]*touching[1][2][0]))
    if len(touching) > 2:
        print(touching)

# print(debugears)
        

sum = 0
for i in range(len(gears)):
    sum += gears[i]

print(sum)




    
    
        