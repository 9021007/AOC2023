import os

input = open("input.txt", "r").read().split("\n")

redmax = 12
greenmax = 13
bluemax = 14

impossible_games = []

powers = []

for i in range(len(input)):
    # print(i)
    # for each game
    id = input[i].split(":")[0].replace("Game ", "")
    data = input[i].split(":")[1].split(";")
    for j in range(len(data)):
        # print(data[j])
        gamedata = data[j].split(",")
        for k in range(len(gamedata)):
            # print(gamedata[k])
            if gamedata[k][-3:] == "red":
                amount = gamedata[k][:-4]
                if int(amount) > redmax:
                    # print("IMPOSSIBLE GAME: " + id + " " + str(amount) + " > " + str(redmax) + "RED")
                    if id not in impossible_games:
                        impossible_games.append(id)
            if gamedata[k][-5:] == "green":
                amount = gamedata[k][:-6]
                if int(amount) > greenmax:
                    # print("IMPOSSIBLE GAME: " + id + " " + str(amount) + " > " + str(greenmax) + "GREEN")
                    if id not in impossible_games:
                        impossible_games.append(id)
            if gamedata[k][-4:] == "blue":
                amount = gamedata[k][:-5]
                if int(amount) > bluemax:
                    # print("IMPOSSIBLE GAME: " + id + " " + str(amount) + " > " + str(bluemax) + "BLUE")
                    if id not in impossible_games:
                        impossible_games.append(id)
    wholegamedata = []
    for j in range(len(data)):
        wholegamedata.append(data[j])
    wholegamedata = ", ".join(wholegamedata)
    wholegamedata = wholegamedata[1:]
    # print(wholegamedata)
    wholegamedata = wholegamedata.split(", ")
    for j in range(len(wholegamedata)):
        if wholegamedata[j][-3:] == "red":
            wholegamedata[j] = ("red", int(wholegamedata[j][:-4]))
        if wholegamedata[j][-5:] == "green":
            wholegamedata[j] = ("green", int(wholegamedata[j][:-6]))
        if wholegamedata[j][-4:] == "blue":
            wholegamedata[j] = ("blue", int(wholegamedata[j][:-5]))
    # print(wholegamedata)

    currentmaxred = 0
    currentmaxgreen = 0
    currentmaxblue = 0

    for j in range(len(wholegamedata)):
        if wholegamedata[j][0] == "red":
            if wholegamedata[j][1] > currentmaxred:
                currentmaxred = wholegamedata[j][1]
        if wholegamedata[j][0] == "green":
            if wholegamedata[j][1] > currentmaxgreen:
                currentmaxgreen = wholegamedata[j][1]
        if wholegamedata[j][0] == "blue":
            if wholegamedata[j][1] > currentmaxblue:
                currentmaxblue = wholegamedata[j][1]
    
    # print("CURRENT MAX RED: " + str(currentmaxred))
    # print("CURRENT MAX GREEN: " + str(currentmaxgreen))
    # print("CURRENT MAX BLUE: " + str(currentmaxblue))

    if currentmaxred == 0:
        currentmaxred = 1
    if currentmaxgreen == 0:
        currentmaxgreen = 1
    if currentmaxblue == 0:
        currentmaxblue = 1

    powers.append(currentmaxred * currentmaxgreen * currentmaxblue)





# print("IMPOSSIBLE GAMES: " + str(impossible_games))


possible_games = []
for i in range(1, 100):
    if str(i) not in impossible_games:
        possible_games.append(str(i))

# sum IDs of possible games
sum = 0
for i in range(len(possible_games)):
    sum += int(possible_games[i])

print("SUM OF POSSIBLE GAMES: " + str(sum))


# sum of powers
sum = 0
for i in range(len(powers)):
    sum += powers[i]

print("SUM OF POWERS: " + str(sum))
    

    
