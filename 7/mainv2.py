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

fiveofakindrepl = []

for i in range(0, len(hands)):
    letters = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    found = False
    # print(i, hands[i])
    for j in range(0, len(letters)):

        if not found:

            tmphand = []
            for k in range(len(hands[i])):
                tmphand.append(hands[i][k].replace("J", letters[j]))
            tmphand.sort()

            if tmphand[0] == tmphand[1] and tmphand[1] == tmphand[2] and tmphand[2] == tmphand[3] and tmphand[3] == tmphand[4]:
                fiveofakindrepl.append((hands[i].replace("J", letters[j]), bids[i]))
                fiveofakind.append((hands[i], bids[i]))
                found = True

for i in range(len(fiveofakind)):
    hands.remove(fiveofakind[i][0])
    bids.remove(fiveofakind[i][1])

print(fiveofakind)
print(fiveofakindrepl)

# four of a kind
 
fourofakindrepl = []

for i in range(0, len(hands)):
    letters = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    found = False
    # print(i, hands[i])
    for j in range(0, len(letters)):

        if not found:

            tmphand = []
            for k in range(len(hands[i])):
                tmphand.append(hands[i][k].replace("J", letters[j]))
            tmphand.sort()

            if tmphand[0] == tmphand[1] and tmphand[1] == tmphand[2] and tmphand[2] == tmphand[3]:
                fourofakindrepl.append((hands[i].replace("J", letters[j]), bids[i]))
                fourofakind.append((hands[i], bids[i]))
                found = True
            if tmphand[1] == tmphand[2] and tmphand[2] == tmphand[3] and tmphand[3] == tmphand[4]:
                fourofakindrepl.append((hands[i].replace("J", letters[j]), bids[i]))
                fourofakind.append((hands[i], bids[i]))
                found = True

for i in range(len(fourofakind)):
    hands.remove(fourofakind[i][0])
    bids.remove(fourofakind[i][1])

print(fourofakind)
print(fourofakindrepl)

# full house

fullhouserepl = []

for i in range(0, len(hands)):
    letters = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    found = False
    # print(i, hands[i])
    for j in range(0, len(letters)):

        if not found:

            tmphand = []
            for k in range(len(hands[i])):
                tmphand.append(hands[i][k].replace("J", letters[j]))
            tmphand.sort()

            if tmphand[0] == tmphand[1] and tmphand[1] == tmphand[2] and tmphand[3] == tmphand[4]:
                fullhouserepl.append((hands[i].replace("J", letters[j]), bids[i]))
                fullhouse.append((hands[i], bids[i]))
                found = True
            if tmphand[0] == tmphand[1] and tmphand[2] == tmphand[3] and tmphand[3] == tmphand[4]:
                fullhouserepl.append((hands[i].replace("J", letters[j]), bids[i]))
                fullhouse.append((hands[i], bids[i]))
                found = True

for i in range(len(fullhouse)):
    hands.remove(fullhouse[i][0])
    bids.remove(fullhouse[i][1])

print(fullhouse)
print(fullhouserepl)

# three of a kind

threeofakindrepl = []

for i in range(0, len(hands)):
    letters = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    found = False
    # print(i, hands[i])
    for j in range(0, len(letters)):

        if not found:

            tmphand = []
            for k in range(len(hands[i])):
                tmphand.append(hands[i][k].replace("J", letters[j]))
            tmphand.sort()

            if tmphand[0] == tmphand[1] and tmphand[1] == tmphand[2]:
                threeofakindrepl.append((hands[i].replace("J", letters[j]), bids[i]))
                threeofakind.append((hands[i], bids[i]))
                found = True
            if tmphand[1] == tmphand[2] and tmphand[2] == tmphand[3]:
                threeofakindrepl.append((hands[i].replace("J", letters[j]), bids[i]))
                threeofakind.append((hands[i], bids[i]))
                found = True
            if tmphand[2] == tmphand[3] and tmphand[3] == tmphand[4]:
                threeofakindrepl.append((hands[i].replace("J", letters[j]), bids[i]))
                threeofakind.append((hands[i], bids[i]))
                found = True

for i in range(len(threeofakind)):
    hands.remove(threeofakind[i][0])
    bids.remove(threeofakind[i][1])

print(threeofakind)
print(threeofakindrepl)

# two pair

twopairrepl = []

for i in range(0, len(hands)):
    letters = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    found = False
    # print(i, hands[i])
    for j in range(0, len(letters)):

        if not found:

            tmphand = []
            for k in range(len(hands[i])):
                tmphand.append(hands[i][k].replace("J", letters[j]))
            tmphand.sort()

            if tmphand[0] == tmphand[1] and tmphand[2] == tmphand[3]:
                twopairrepl.append((hands[i].replace("J", letters[j]), bids[i]))
                twopair.append((hands[i], bids[i]))
                found = True
            if tmphand[0] == tmphand[1] and tmphand[3] == tmphand[4]:
                twopairrepl.append((hands[i].replace("J", letters[j]), bids[i]))
                twopair.append((hands[i], bids[i]))
                found = True
            if tmphand[1] == tmphand[2] and tmphand[3] == tmphand[4]:
                twopairrepl.append((hands[i].replace("J", letters[j]), bids[i]))
                twopair.append((hands[i], bids[i]))
                found = True

for i in range(len(twopair)):
    hands.remove(twopair[i][0])
    bids.remove(twopair[i][1])

print(twopair)
print(twopairrepl)

# one pair

onepairrepl = []

for i in range(0, len(hands)):
    letters = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    found = False
    # print(i, hands[i])
    for j in range(0, len(letters)):

        if not found:

            tmphand = []
            for k in range(len(hands[i])):
                tmphand.append(hands[i][k].replace("J", letters[j]))
            tmphand.sort()

            if tmphand[0] == tmphand[1]:
                onepairrepl.append((hands[i].replace("J", letters[j]), bids[i]))
                onepair.append((hands[i], bids[i]))
                found = True
            if tmphand[1] == tmphand[2]:
                onepairrepl.append((hands[i].replace("J", letters[j]), bids[i]))
                onepair.append((hands[i], bids[i]))
                found = True
            if tmphand[2] == tmphand[3]:
                onepairrepl.append((hands[i].replace("J", letters[j]), bids[i]))
                onepair.append((hands[i], bids[i]))
                found = True
            if tmphand[3] == tmphand[4]:
                onepairrepl.append((hands[i].replace("J", letters[j]), bids[i]))
                onepair.append((hands[i], bids[i]))
                found = True

for i in range(len(onepair)):
    hands.remove(onepair[i][0])
    bids.remove(onepair[i][1])

print(onepair)
print(onepairrepl)

# high card

highcardrepl = []

for i in range(0, len(hands)):
    letters = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    found = False
    # print(i, hands[i])
    for j in range(0, len(letters)):

        if not found:

            tmphand = []
            for k in range(len(hands[i])):
                tmphand.append(hands[i][k].replace("J", letters[j]))
            tmphand.sort()

            highcardrepl.append((hands[i].replace("J", letters[j]), bids[i]))
            highcard.append((hands[i], bids[i]))
            found = True

for i in range(len(highcard)):
    hands.remove(highcard[i][0])
    bids.remove(highcard[i][1])

print(highcard)
print(highcardrepl)

# print(highcard)

# sorting

sorttmp = []

for i in range(0, len(fiveofakind)):
    tmphand = fiveofakind[i][0].replace("K", "B").replace("Q", "C").replace("T", "E").replace("9", "F").replace("8", "G").replace("7", "H").replace("6", "I").replace("5", "L").replace("4", "M").replace("3", "N").replace("2", "O").replace("J", "P")
    sorttmp.append((tmphand, fiveofakind[i][1]))

newsorted = sorted(sorttmp, key=lambda x: x[0])

fiveofakind = []

for i in range(0, len(newsorted)):
    tmphand = newsorted[i][0].replace("B", "K").replace("C", "Q").replace("E", "T").replace("F", "9").replace("G", "8").replace("H", "7").replace("I", "6").replace("L", "5").replace("M", "4").replace("N", "3").replace("O", "2").replace("P", "J")
    fiveofakind.append((tmphand, newsorted[i][1]))

sorttmp = []

# print(fiveofakind)

# four of a kind

for i in range(0, len(fourofakind)):
    tmphand = fourofakind[i][0].replace("K", "B").replace("Q", "C").replace("T", "E").replace("9", "F").replace("8", "G").replace("7", "H").replace("6", "I").replace("5", "L").replace("4", "M").replace("3", "N").replace("2", "O").replace("J", "P")
    sorttmp.append((tmphand, fourofakind[i][1]))

newsorted = sorted(sorttmp, key=lambda x: x[0])

fourofakind = []

for i in range(0, len(newsorted)):
    tmphand = newsorted[i][0].replace("B", "K").replace("C", "Q").replace("E", "T").replace("F", "9").replace("G", "8").replace("H", "7").replace("I", "6").replace("L", "5").replace("M", "4").replace("N", "3").replace("O", "2").replace("P", "J")
    fourofakind.append((tmphand, newsorted[i][1]))

sorttmp = []

# full house

for i in range(0, len(fullhouse)):
    tmphand = fullhouse[i][0].replace("K", "B").replace("Q", "C").replace("T", "E").replace("9", "F").replace("8", "G").replace("7", "H").replace("6", "I").replace("5", "L").replace("4", "M").replace("3", "N").replace("2", "O").replace("J", "P")
    sorttmp.append((tmphand, fullhouse[i][1]))

newsorted = sorted(sorttmp, key=lambda x: x[0])

fullhouse = []

for i in range(0, len(newsorted)):
    tmphand = newsorted[i][0].replace("B", "K").replace("C", "Q").replace("E", "T").replace("F", "9").replace("G", "8").replace("H", "7").replace("I", "6").replace("L", "5").replace("M", "4").replace("N", "3").replace("O", "2").replace("P", "J")
    fullhouse.append((tmphand, newsorted[i][1]))

sorttmp = []

# three of a kind

for i in range(0, len(threeofakind)):
    tmphand = threeofakind[i][0].replace("K", "B").replace("Q", "C").replace("T", "E").replace("9", "F").replace("8", "G").replace("7", "H").replace("6", "I").replace("5", "L").replace("4", "M").replace("3", "N").replace("2", "O").replace("J", "P")
    sorttmp.append((tmphand, threeofakind[i][1]))

newsorted = sorted(sorttmp, key=lambda x: x[0])

threeofakind = []

for i in range(0, len(newsorted)):
    tmphand = newsorted[i][0].replace("B", "K").replace("C", "Q").replace("E", "T").replace("F", "9").replace("G", "8").replace("H", "7").replace("I", "6").replace("L", "5").replace("M", "4").replace("N", "3").replace("O", "2").replace("P", "J")
    threeofakind.append((tmphand, newsorted[i][1]))

sorttmp = []

# two pair

for i in range(0, len(twopair)):
    tmphand = twopair[i][0].replace("K", "B").replace("Q", "C").replace("T", "E").replace("9", "F").replace("8", "G").replace("7", "H").replace("6", "I").replace("5", "L").replace("4", "M").replace("3", "N").replace("2", "O").replace("J", "P")
    sorttmp.append((tmphand, twopair[i][1]))

newsorted = sorted(sorttmp, key=lambda x: x[0])

twopair = []

for i in range(0, len(newsorted)):
    tmphand = newsorted[i][0].replace("B", "K").replace("C", "Q").replace("E", "T").replace("F", "9").replace("G", "8").replace("H", "7").replace("I", "6").replace("L", "5").replace("M", "4").replace("N", "3").replace("O", "2").replace("P", "J")
    twopair.append((tmphand, newsorted[i][1]))

sorttmp = []

# one pair

for i in range(0, len(onepair)):
    tmphand = onepair[i][0].replace("K", "B").replace("Q", "C").replace("T", "E").replace("9", "F").replace("8", "G").replace("7", "H").replace("6", "I").replace("5", "L").replace("4", "M").replace("3", "N").replace("2", "O").replace("J", "P")
    sorttmp.append((tmphand, onepair[i][1]))

newsorted = sorted(sorttmp, key=lambda x: x[0])

onepair = []

for i in range(0, len(newsorted)):
    tmphand = newsorted[i][0].replace("B", "K").replace("C", "Q").replace("E", "T").replace("F", "9").replace("G", "8").replace("H", "7").replace("I", "6").replace("L", "5").replace("M", "4").replace("N", "3").replace("O", "2").replace("P", "J")
    onepair.append((tmphand, newsorted[i][1]))

sorttmp = []

# high card

for i in range(0, len(highcard)):
    tmphand = highcard[i][0].replace("K", "B").replace("Q", "C").replace("T", "E").replace("9", "F").replace("8", "G").replace("7", "H").replace("6", "I").replace("5", "L").replace("4", "M").replace("3", "N").replace("2", "O").replace("J", "P")
    sorttmp.append((tmphand, highcard[i][1]))

newsorted = sorted(sorttmp, key=lambda x: x[0])

highcard = []

for i in range(0, len(newsorted)):
    tmphand = newsorted[i][0].replace("B", "K").replace("C", "Q").replace("E", "T").replace("F", "9").replace("G", "8").replace("H", "7").replace("I", "6").replace("L", "5").replace("M", "4").replace("N", "3").replace("O", "2").replace("P", "J")
    highcard.append((tmphand, newsorted[i][1]))

sorttmp = []

# print(fiveofakind)


allsorted = fiveofakind + fourofakind + fullhouse + threeofakind + twopair + onepair + highcard


# print(allsorted)

sum = 0

for i in range(0, len(allsorted)):
    rank = len(allsorted) - i
    sum += rank * int(allsorted[i][1])

print(sum)
