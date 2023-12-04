import os

input = open(os.path.abspath(os.path.dirname(__file__)) + '/input.txt', 'r')

input = input.read().split('\n')

output = [""]

for i in range(len(input)):



    temp = list(input[i])
    for j in range(len(temp)):
        if str(temp[j]).isdigit():
            pass
        else:
            if input[i][j:j+3] == "one":
                temp[j] = "1"
            elif input[i][j:j+3] == "two":
                temp[j] = "2"
            elif input[i][j:j+5] == "three":
                temp[j] = "3"
            elif input[i][j:j+4] == "four":
                temp[j] = "4"
            elif input[i][j:j+4] == "five":
                temp[j] = "5"
            elif input[i][j:j+3] == "six":
                temp[j] = "6"
            elif input[i][j:j+5] == "seven":
                temp[j] = "7"
            elif input[i][j:j+5] == "eight":
                temp[j] = "8"
            elif input[i][j:j+4] == "nine":
                temp[j] = "9"
            elif input[i][j:j+4] == "zero":
                temp[j] = "0"
            else:
                temp[j] = ""
    print(str(i) + ": " + str(temp))

    combined = "".join(temp)
    output.append(str(combined[:1]+""+combined[-1:]))
    # print(combined[:1]+""+combined[-1:])

sum = 0
for i in range(len(output)):
    if str(output[i]).isdigit():
        sum += int(output[i])

print(sum)