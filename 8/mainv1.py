input = open("input.txt", "r").read().split("\n")

instructions = input[0]

nodes = input[2:]

# print(instructions)
# print(nodes)

stepcount = 0

nodeobj = {}

for i in range(len(nodes)):
    # print(nodes[i])
    nodeobj[nodes[i][:3]] = {
            "L": nodes[i][7:10],
            "R": nodes[i][12:15]
        }
    
    
# print(nodeobj)

atend = False
currentid = "AAA"

while atend == False:
    for i in range(len(instructions)):
        if currentid == "ZZZ":
            atend = True
            # print("FOUND")
            break
        else:
            stepcount = stepcount + 1
            currentid = nodeobj[currentid][instructions[i]]
            # print(currentid)

print(stepcount)