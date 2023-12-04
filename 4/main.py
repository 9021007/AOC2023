import os
import time
from sys import getsizeof

### this code is a crime against humanity.

### please avert your eyes.

### i am ashamed to have written it.

start_time = time.time()

input = open("input.txt", "r").read().split("\n")

cards = []
winners = []

# cardnum, targets, numbers

for i in range(len(input)):
    id = int(str(input[i][5:8]).replace(" ",""))
    # print(id)
    targets = list(filter(None, input[i][10:40].split(" ")))
    # print(targets)
    numbers = list(filter(None, input[i][42:116].split(" ")))
    # print(numbers)
    cards.append((id, targets, numbers))

for i in range(len(cards)):
    matches = []
    for j in range(len(cards[i][2])):
        if cards[i][2][j] in cards[i][1]:
            # print("match", cards[i][0])
            matches.append(cards[i][2][j])
    # print("matching", cards[i][0], len(matches))
    
    winners.append((cards[i][0],(len(matches))))

# print(winners)

cards2 = []

for i in range(len(winners)):
    cards2.append(winners[i][0])

# print(cards2)

for i in range(len(winners)):
    instances = cards2.count(winners[i][0])
    # print(winners[i][0], "appears", cards2.count(winners[i][0]), "times")
    for j in range(instances):
        for k in range(winners[i][1]):
            cards2.append(winners[i][0]+1+k)
    # print(len(cards2), winners[i][0])

print("DONE " + str(len(cards2)) + " MATCHES IN " + str(time.time() - start_time) + " SECONDS, taking up " + str(getsizeof(cards2)) + " bytes of memory")
    
