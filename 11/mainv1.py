from tqdm import tqdm


# input = open("input.txt", "r").read().split("\n")
input = open("exampleinput.txt", "r").read().split("\n")

preexpand = []

for line in input:
    preexpand.append(list(line))

# print(preexpand)

expanded1 = []

for i in range(len(preexpand)):
    # for each row in unexpanded1
    if list(set(preexpand[i])) == ["."]:
        # if the row is only stars
        expanded1.append([])
        expanded1.append([])
        for j in range(len(preexpand[i])):
            #for each dot star
            expanded1[len(expanded1)-1].append(".")
            expanded1[len(expanded1)-2].append(".")
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
            if expanded1[i][j] != ".":
                dotsonly.remove(j)
                # print("removed ", j, " at line ", i)

print(dotsonly)

# for i in range(len(dotsonly)):
for j in range(len(expanded1)):
    expanded2.append([])
    
    for k in range(len(expanded1[j])):
        if k in dotsonly:
            expanded2[j].append(".")
            expanded2[j].append(".")
            # print(expanded2)
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
        g[2].append([other[0], other[1], abs(g[0]-other[0])+abs(g[1]-other[1])])

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


