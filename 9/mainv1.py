input = open("input.txt", "r").read().split("\n")
# input = open("exampleinput.txt", "r").read().split("\n")




sequences = []

for line in input:
    sequences.append([line.split(" ")])

def calcDiffereces():
    for sequence in sequences:
        differences = []
        currentlen = len(sequence)
        if list(set(sequence[currentlen-1])) == [0]:
            # print("ALL ZEROES")
            pass
        else:
            for i in range(len(sequence[currentlen-1])-1):
                differences.append(int(sequence[currentlen-1][i+1])-int(sequence[currentlen-1][i]))
            sequence.append(differences)
        # print(list(set(sequence[currentlen-1])))


for i in range(999):
    calcDiffereces()


values = []

# print(sequences)


for seq in sequences:
    # print(" ")
    # print(seq)
    # print("LENGTH: ", len(seq))
    seqlen = len(seq)
    currentval = 0
    for i in reversed(range(seqlen)):
        # print(seq[i-1])
        # print(currentval, " + ", seq[i-1][-1], " = ", currentval+int(str(seq[i-1][-1])))
        currentval = currentval+int(str(seq[i-1][-1]))

    values.append(currentval)

# print("values: ", values)

sum = 0

for val in values:
    sum = sum + val

print(sum)
       






    

# print(sequences)

    
