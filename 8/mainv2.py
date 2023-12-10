from math import lcm
from tqdm import tqdm

input = open("input.txt", "r").read().split("\n")

instructions = input[0]

nodes = input[2:]

# print(instructions)
# print(nodes)

stepcount = 0

nodeobj = {}

currentid = []


for i in range(len(nodes)):
    # print(nodes[i])
    nodeobj[nodes[i][:3]] = {
            "L": nodes[i][7:10],
            "R": nodes[i][12:15]
        }
    if nodes[i][2] == "A":
        # print("ENDING", nodes[i])
        currentid.append(nodes[i][:3])
    


looplength = []

atend = False
# currentid = "AAA"

# print(currentid)

for j in range(len(currentid)):
    # print("checking", currentid[j])
    atend = False
    tmpcid = currentid[j]
    tmpcidi = currentid[j]
    while atend == False:
        for i in range(len(instructions)):
            if atend == False:
                if tmpcid[2] == "Z":
                    atend = True
                    # print("FOUND")
                    looplength.append(stepcount)
                    stepcount = 0
                else:
                    stepcount = stepcount + 1
                    tmpcid = nodeobj[tmpcid][instructions[i]]
                    # print(tmpcid)

# print(looplength)
        
print(lcm(looplength[0], looplength[1], looplength[2], looplength[3], looplength[4], looplength[5]))

