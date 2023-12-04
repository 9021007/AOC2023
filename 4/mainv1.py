import os

input = open("input.txt", "r").read().split("\n")

cards = []
winners = []

# cardnum, targets, numbers

for i in range(len(input)):
    id = int(str(input[i][5:8]).replace(" ",""))
    print(id)
    targets = list(filter(None, input[i][10:40].split(" ")))
    print(targets)
    numbers = list(filter(None, input[i][42:116].split(" ")))
    print(numbers)
    cards.append((id, targets, numbers))

for i in range(len(cards)):
    matches = []
    for j in range(len(cards[i][2])):
        if cards[i][2][j] in cards[i][1]:
            print("match", cards[i][0])
            matches.append(cards[i][2][j])
    print("matching", cards[i][0], len(matches))
    if len(matches) != 0:
        winners.append((cards[i][0],2**(len(matches)-1)))

sum = 0
for i in range(len(winners)):
    sum += winners[i][1]
print(sum)
print(winners)
print(len(winners))

