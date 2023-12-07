import os

# input = open("exampleinput.txt", "r").read().split("\n")
input = open("input.txt", "r").read().split("\n")

hands = []
bids = []

for i in range(0, len(input)):
    hands.append(input[i].split(" ")[0])
    bids.append(input[i].split(" ")[1])

hands2 = hands

# print(hands)
# print(bids)

fiveofakind = []
fourofakind = []
fullhouse = []
threeofakind = []
twopair = []
onepair = []
highcard = []

#five of a kind

for i in range(0, len(hands)):
    if hands[i][0] == hands[i][1] and hands[i][1] == hands[i][2] and hands[i][2] == hands[i][3] and hands[i][3] == hands[i][4]:
        fiveofakind.append((hands[i], bids[i]))

for i in range(len(fiveofakind)):
    hands.remove(fiveofakind[i][0])
    bids.remove(fiveofakind[i][1])

# print(fiveofakind)

# four of a kind

for i in range(0, len(hands)):
    tmphand = []
    for j in range(len(hands[i])):
        tmphand.append(hands[i][j])
    tmphand.sort()
    if tmphand[0] == tmphand[1] and tmphand[1] == tmphand[2] and tmphand[2] == tmphand[3]:
        fourofakind.append((hands[i], bids[i]))
    if tmphand[1] == tmphand[2] and tmphand[2] == tmphand[3] and tmphand[3] == tmphand[4]:
        fourofakind.append((hands[i], bids[i]))

for i in range(len(fourofakind)):
    hands.remove(fourofakind[i][0])
    bids.remove(fourofakind[i][1])

# print(fourofakind)

# full house

for i in range(0, len(hands)):
    tmphand = []
    for j in range(len(hands[i])):
        tmphand.append(hands[i][j])
    tmphand.sort()
    if tmphand[0] == tmphand[1] and tmphand[1] == tmphand[2] and tmphand[3] == tmphand[4]:
        fullhouse.append((hands[i], bids[i]))
    if tmphand[0] == tmphand[1] and tmphand[2] == tmphand[3] and tmphand[3] == tmphand[4]:
        fullhouse.append((hands[i], bids[i]))

for i in range(len(fullhouse)):
    hands.remove(fullhouse[i][0])
    bids.remove(fullhouse[i][1])

# print(fullhouse)

# three of a kind

for i in range(0, len(hands)):
    tmphand = []
    for j in range(len(hands[i])):
        tmphand.append(hands[i][j])
    tmphand.sort()
    if tmphand[0] == tmphand[1] and tmphand[1] == tmphand[2]:
        threeofakind.append((hands[i], bids[i]))
    if tmphand[1] == tmphand[2] and tmphand[2] == tmphand[3]:
        threeofakind.append((hands[i], bids[i]))
    if tmphand[2] == tmphand[3] and tmphand[3] == tmphand[4]:
        threeofakind.append((hands[i], bids[i]))
    
for i in range(len(threeofakind)):
    hands.remove(threeofakind[i][0])
    bids.remove(threeofakind[i][1])

# print(threeofakind)

# two pair

for i in range(0, len(hands)):
    tmphand = []
    for j in range(len(hands[i])):
        tmphand.append(hands[i][j])
    tmphand.sort()
    if tmphand[0] == tmphand[1] and tmphand[2] == tmphand[3]:
        twopair.append((hands[i], bids[i]))
    if tmphand[0] == tmphand[1] and tmphand[3] == tmphand[4]:
        twopair.append((hands[i], bids[i]))
    if tmphand[1] == tmphand[2] and tmphand[3] == tmphand[4]:
        twopair.append((hands[i], bids[i]))
    
for i in range(len(twopair)):
    hands.remove(twopair[i][0])
    bids.remove(twopair[i][1])

# print(twopair)

# one pair

for i in range(0, len(hands)):
    tmphand = []
    for j in range(len(hands[i])):
        tmphand.append(hands[i][j])
    tmphand.sort()
    if tmphand[0] == tmphand[1]:
        onepair.append((hands[i], bids[i]))
    if tmphand[1] == tmphand[2]:
        onepair.append((hands[i], bids[i]))
    if tmphand[2] == tmphand[3]:
        onepair.append((hands[i], bids[i]))
    if tmphand[3] == tmphand[4]:
        onepair.append((hands[i], bids[i]))

for i in range(len(onepair)):
    hands.remove(onepair[i][0])
    bids.remove(onepair[i][1])

# print(onepair)

# high card

for i in range(0, len(hands)):
    highcard.append((hands[i], bids[i]))

# print(highcard)

# sorting

sorttmp = []

for i in range(0, len(fiveofakind)):
    tmphand = fiveofakind[i][0].replace("K", "B").replace("Q", "C").replace("J", "D").replace("T", "E").replace("9", "F").replace("8", "G").replace("7", "H").replace("6", "I").replace("5", "L").replace("4", "M").replace("3", "N").replace("2", "O")
    sorttmp.append((tmphand, fiveofakind[i][1]))

newsorted = sorted(sorttmp, key=lambda x: x[0])

fiveofakind = []

for i in range(0, len(newsorted)):
    tmphand = newsorted[i][0].replace("B", "K").replace("C", "Q").replace("D", "J").replace("E", "T").replace("F", "9").replace("G", "8").replace("H", "7").replace("I", "6").replace("L", "5").replace("M", "4").replace("N", "3").replace("O", "2")
    fiveofakind.append((tmphand, newsorted[i][1]))

sorttmp = []

# print(fiveofakind)

# four of a kind

for i in range(0, len(fourofakind)):
    tmphand = fourofakind[i][0].replace("K", "B").replace("Q", "C").replace("J", "D").replace("T", "E").replace("9", "F").replace("8", "G").replace("7", "H").replace("6", "I").replace("5", "L").replace("4", "M").replace("3", "N").replace("2", "O")
    sorttmp.append((tmphand, fourofakind[i][1]))

newsorted = sorted(sorttmp, key=lambda x: x[0])

fourofakind = []

for i in range(0, len(newsorted)):
    tmphand = newsorted[i][0].replace("B", "K").replace("C", "Q").replace("D", "J").replace("E", "T").replace("F", "9").replace("G", "8").replace("H", "7").replace("I", "6").replace("L", "5").replace("M", "4").replace("N", "3").replace("O", "2")
    fourofakind.append((tmphand, newsorted[i][1]))

sorttmp = []

# print(fourofakind)

# full house

for i in range(0, len(fullhouse)):
    tmphand = fullhouse[i][0].replace("K", "B").replace("Q", "C").replace("J", "D").replace("T", "E").replace("9", "F").replace("8", "G").replace("7", "H").replace("6", "I").replace("5", "L").replace("4", "M").replace("3", "N").replace("2", "O")
    sorttmp.append((tmphand, fullhouse[i][1]))

newsorted = sorted(sorttmp, key=lambda x: x[0])

fullhouse = []

for i in range(0, len(newsorted)):
    tmphand = newsorted[i][0].replace("B", "K").replace("C", "Q").replace("D", "J").replace("E", "T").replace("F", "9").replace("G", "8").replace("H", "7").replace("I", "6").replace("L", "5").replace("M", "4").replace("N", "3").replace("O", "2")
    fullhouse.append((tmphand, newsorted[i][1]))

sorttmp = []

# print(fullhouse)

# three of a kind

for i in range(0, len(threeofakind)):
    tmphand = threeofakind[i][0].replace("K", "B").replace("Q", "C").replace("J", "D").replace("T", "E").replace("9", "F").replace("8", "G").replace("7", "H").replace("6", "I").replace("5", "L").replace("4", "M").replace("3", "N").replace("2", "O")
    sorttmp.append((tmphand, threeofakind[i][1]))

newsorted = sorted(sorttmp, key=lambda x: x[0])

threeofakind = []

for i in range(0, len(newsorted)):
    tmphand = newsorted[i][0].replace("B", "K").replace("C", "Q").replace("D", "J").replace("E", "T").replace("F", "9").replace("G", "8").replace("H", "7").replace("I", "6").replace("L", "5").replace("M", "4").replace("N", "3").replace("O", "2")
    threeofakind.append((tmphand, newsorted[i][1]))

sorttmp = []

# print(threeofakind)

# two pair

for i in range(0, len(twopair)):
    tmphand = twopair[i][0].replace("K", "B").replace("Q", "C").replace("J", "D").replace("T", "E").replace("9", "F").replace("8", "G").replace("7", "H").replace("6", "I").replace("5", "L").replace("4", "M").replace("3", "N").replace("2", "O")
    sorttmp.append((tmphand, twopair[i][1]))

newsorted = sorted(sorttmp, key=lambda x: x[0])

twopair = []

for i in range(0, len(newsorted)):
    tmphand = newsorted[i][0].replace("B", "K").replace("C", "Q").replace("D", "J").replace("E", "T").replace("F", "9").replace("G", "8").replace("H", "7").replace("I", "6").replace("L", "5").replace("M", "4").replace("N", "3").replace("O", "2")
    twopair.append((tmphand, newsorted[i][1]))

sorttmp = []

# print(twopair)

# one pair

for i in range(0, len(onepair)):
    tmphand = onepair[i][0].replace("K", "B").replace("Q", "C").replace("J", "D").replace("T", "E").replace("9", "F").replace("8", "G").replace("7", "H").replace("6", "I").replace("5", "L").replace("4", "M").replace("3", "N").replace("2", "O")
    sorttmp.append((tmphand, onepair[i][1]))

newsorted = sorted(sorttmp, key=lambda x: x[0])

onepair = []

for i in range(0, len(newsorted)):
    tmphand = newsorted[i][0].replace("B", "K").replace("C", "Q").replace("D", "J").replace("E", "T").replace("F", "9").replace("G", "8").replace("H", "7").replace("I", "6").replace("L", "5").replace("M", "4").replace("N", "3").replace("O", "2")
    onepair.append((tmphand, newsorted[i][1]))

sorttmp = []

# print(onepair)

# high card

for i in range(0, len(highcard)):
    tmphand = highcard[i][0].replace("K", "B").replace("Q", "C").replace("J", "D").replace("T", "E").replace("9", "F").replace("8", "G").replace("7", "H").replace("6", "I").replace("5", "L").replace("4", "M").replace("3", "N").replace("2", "O")
    sorttmp.append((tmphand, highcard[i][1]))

newsorted = sorted(sorttmp, key=lambda x: x[0])

highcard = []

for i in range(0, len(newsorted)):
    tmphand = newsorted[i][0].replace("B", "K").replace("C", "Q").replace("D", "J").replace("E", "T").replace("F", "9").replace("G", "8").replace("H", "7").replace("I", "6").replace("L", "5").replace("M", "4").replace("N", "3").replace("O", "2")
    highcard.append((tmphand, newsorted[i][1]))

sorttmp = []

# print(highcard)

allsorted = fiveofakind + fourofakind + fullhouse + threeofakind + twopair + onepair + highcard

sum = 0

for i in range(0, len(allsorted)):
    rank = len(allsorted) - i
    sum += rank * int(allsorted[i][1])

print(sum)
