from PIL import Image
import numpy as np
import math

# THIS IS THE SECOND OF TWO PART 2 SCRIPTS, USE MAINV2IMG.PY FOR THE FIRST PART
# THIS IS THE SECOND OF TWO PART 2 SCRIPTS, USE MAINV2IMG.PY FOR THE FIRST PART
# THIS IS THE SECOND OF TWO PART 2 SCRIPTS, USE MAINV2IMG.PY FOR THE FIRST PART
# THIS IS THE SECOND OF TWO PART 2 SCRIPTS, USE MAINV2IMG.PY FOR THE FIRST PART
# THIS IS THE SECOND OF TWO PART 2 SCRIPTS, USE MAINV2IMG.PY FOR THE FIRST PART
# THIS IS THE SECOND OF TWO PART 2 SCRIPTS, USE MAINV2IMG.PY FOR THE FIRST PART
# THIS IS THE SECOND OF TWO PART 2 SCRIPTS, USE MAINV2IMG.PY FOR THE FIRST PART
# THIS IS THE SECOND OF TWO PART 2 SCRIPTS, USE MAINV2IMG.PY FOR THE FIRST PART
# THIS IS THE SECOND OF TWO PART 2 SCRIPTS, USE MAINV2IMG.PY FOR THE FIRST PART
# THIS IS THE SECOND OF TWO PART 2 SCRIPTS, USE MAINV2IMG.PY FOR THE FIRST PART
# THIS IS THE SECOND OF TWO PART 2 SCRIPTS, USE MAINV2IMG.PY FOR THE FIRST PART
# THIS IS THE SECOND OF TWO PART 2 SCRIPTS, USE MAINV2IMG.PY FOR THE FIRST PART

count = 0

with Image.open("imgout.png") as pilimg:
    img = np.asarray(pilimg).copy()
    print(np.asarray(img[0][0]))
    print([253,9,9,255])
    print((img[0][0] == [253,9,9,255]).all())

    for i in range(math.floor(len(img)/3)):
        for j in range(math.floor(len(img[i])/3)):
            if img[i*3][j*3][0] == 255:
                passing = True
                target = [253,8,8,255]
                if (img[i*3+3][j*3] == target).all():
                    passing = False
                if (img[i*3][j*3+3] == target).all():
                    passing = False
                if (img[i*3-1][j*3] == target).all():
                    passing = False
                if (img[i*3][j*3-1] == target).all():
                    passing = False
                if passing:
                    print(i, j)
                    print(" ")
                    count += 1
                    img[i*3][j*3] = [50,50,50,255]
                    img[i*3+1][j*3] = [50,50,50,255]
                    img[i*3+2][j*3] = [50,50,50,255]
                    img[i*3][j*3+1] = [50,50,50,255]
                    img[i*3+1][j*3+1] = [50,50,50,255]
                    img[i*3+2][j*3+1] = [50,50,50,255]
                    img[i*3][j*3+2] = [50,50,50,255]
                    img[i*3+1][j*3+2] = [50,50,50,255]
                    img[i*3+2][j*3+2] = [50,50,50,255]

    newimg = Image.fromarray(img)
    newimg.save("imgout2.png")

print(count)