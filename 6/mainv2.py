import os

# pre = open("exampleinput.txt", "r").read().split("\n")
pre = open("inputv2.txt", "r").read().split("\n")

times = []
distances = []
wintimesounts= []

for i in range(len(pre)):
    tmp = pre[i].split(" ")
    for j in range(len(tmp)):
        if i == 0 and tmp[j] != "":
            times.append(tmp[j])
        elif i == 1 and tmp[j] != "":
            distances.append(tmp[j])

times.pop(0)
distances.pop(0)

print(times)
print(distances)

for i in range(len(times)):
    lowesttime = 9999999999999999
    highesttime = 0
    currenttriedtime = 0
    lowfound = False
    currenthold = 0
    while lowfound == False:
        print("trying", currenthold)
        if (int(times[i])-currenthold)*currenthold > int(distances[i]):
            lowesttime = currenthold
            lowfound = True
            print("FOUND LOW", currenthold)
        else:
            currenthold = currenthold + 1

    highfound = False
    currenthold = 60000000
    while highfound == False:
        print("trying", currenthold)
        if (int(times[i])-currenthold)*currenthold > int(distances[i]):
            highesttime = currenthold
            highfound = True
            print("FOUND HIGH")
        else:
            currenthold = currenthold - 1

    print("number of winnable times:", highesttime - lowesttime)
    wintimesounts.append((lowesttime, highesttime, (highesttime - lowesttime) + 1))

print(wintimesounts)
total = 1
for i in range(len(wintimesounts)):
    total = total * wintimesounts[i][2]

print("total:", total)


        
    
    
    
    