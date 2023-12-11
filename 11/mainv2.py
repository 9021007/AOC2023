from tqdm import tqdm


input = open("input.txt", "r").read().split("\n")
# input = open("exampleinput.txt", "r").read().split("\n")

preexpand = []

for line in input:
    preexpand.append(list(line))

# print(preexpand)

expanded1 = []

expansionamount = 1000000

for i in tqdm(range(len(preexpand))):
    # for each row in unexpanded1
    if list(set(preexpand[i])) == ["."]:
        # if the row is only stars
        expanded1.append([])
        for k in range(len(preexpand[i])):
            expanded1[len(expanded1)-1].append("E")
    else:
        expanded1.append([])
        for j in range(len(preexpand[i])):
            expanded1[len(expanded1)-1].append(preexpand[i][j])



expanded2 = []

dotsonly = []

for i in range(len(expanded1[0])):
    if expanded1[0][i] == ".":
        dotsonly.append(i)

for i in range(len(expanded1)):
    for j in range(len(expanded1[i])):
        if j in dotsonly:
            if expanded1[i][j] != "." and expanded1[i][j] != "E":
                dotsonly.remove(j)
                # print("removed ", j, " at line ", i)

print(dotsonly)

# for i in range(len(dotsonly)):
for j in range(len(expanded1)):
    expanded2.append([])
    
    for k in range(len(expanded1[j])):
        if k in dotsonly:
            expanded2[j].append("E")
            # print("E2E2E2E2E2E2")
        else:
            # print(j,k, len(expanded1[j]), len(expanded1[j][k]))
            expanded2[j].append(expanded1[j][k])
            # print(expanded2)


galaxies = []
sum = 0
accountedfor = []
        

# for line in expanded2:
#     print(str(line).replace(" ", "").replace(",", "").replace("'", "").replace("]", "").replace("[", ""))

for i in range(len(expanded2)):
    for j in range(len(expanded2[i])):
        if expanded2[i][j] == "#":

            galaxies.append([i,j,[]])
            # print(galaxies)



for g in galaxies:
    for other in galaxies:
        contents = []
        # find taxicab distance, and return the content of every point along the way

        # Xcontents = expanded2[g[0]][g[1]:other[1]]
        # Ycontents = []
        # for i in range(g[0], other[0]):
        #     Ycontents.append(expanded2[i][other[1]])
        # print(Xcontents, Ycontents)
        Xcontents = []
        if g[1] < other[1]:
            # g is left of other
            Xcontents = expanded2[g[0]][g[1]:other[1]]
            # print(Xcontents, "L")
        elif g[1] == other[1]:
            Xcontents = []
            # print(Xcontents, "S")
        else:
            # g is right of other
            Xcontents = expanded2[g[0]][other[1]:g[1]]
            # print(Xcontents, "R")


        Ycontents = []
        if g[0] < other[0]:
            # g is above other
            for i in range(g[0], other[0]):
                Ycontents.append(expanded2[i][other[1]])
            # print(Ycontents, "U")
        elif g[0] == other[0]:
            Ycontents = []
            # print(Ycontents, "S")
        else:
            # g is below other
            for i in range(other[0], g[0]):
                Ycontents.append(expanded2[i][other[1]])
            # print(Ycontents, "D")
        
        # distance is counted as the number of points between the two galaxies, but E counts as expansionamount points

        Xdistance = Xcontents.count("E")*expansionamount + Xcontents.count("#") + Xcontents.count(".")
        Ydistance = Ycontents.count("E")*expansionamount + Ycontents.count("#") + Ycontents.count(".")

        taxicabdistance = Xdistance + Ydistance

        galaxies[galaxies.index(g)][2].append([other[0], other[1], taxicabdistance])

# for g in galaxies:
#     print(g)

for i in tqdm(range(len(galaxies))):
    for j in range(len(galaxies[i][2])):
        # for each distance
        if (galaxies[i][2][j][0], galaxies[i][2][j][1], galaxies[i][0], galaxies[i][1]) not in accountedfor:
            accountedfor.append((galaxies[i][0], galaxies[i][1], galaxies[i][2][j][0], galaxies[i][2][j][1]))
            sum += galaxies[i][2][j][2]
            # print(galaxies[i], galaxies[i][2][j][0], galaxies[i][2][j][1], galaxies[i][2][j][2])

print(sum)
print(len(accountedfor))
# print(accountedfor)


