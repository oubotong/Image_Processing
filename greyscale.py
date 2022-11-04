from PIL import Image
import os
import cv2 as cv
import numpy as np

path = "C://Users//Richa//Downloads//deblur//output"
dir_list = os.listdir(path)
os.mkdir("./gray")
os.mkdir("./origin")
os.mkdir("./0.7bright_gray")
os.mkdir("./0.7bright_origin")
for image in dir_list:
    img = cv.imread(path + "//" + image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cols, rows = img.shape[0:2]
    brightness = np.sum(img) / (255 * cols * rows)
    ratio = brightness / 0.7
    final_img = cv.convertScaleAbs(img, alpha = 1 / ratio, beta = 0)
    final_gray = cv.convertScaleAbs(gray, alpha = 1 / ratio, beta = 0)
    cv.imwrite("C://Users//Richa//Desktop//Greyscale//gray//" + image + ".jpg", gray)
    cv.imwrite("C://Users//Richa//Desktop//Greyscale//origin//" + image + ".jpg", img)
    cv.imwrite("C://Users//Richa//Desktop//Greyscale//0.7bright_gray//" + image + ".jpg", final_gray)
    cv.imwrite("C://Users//Richa//Desktop//Greyscale//0.7bright_origin//" + image + ".jpg", final_img)

#cv.imshow('Gray image', gray)
#cv.imshow('Final image', final)
#cv.waitKey(0)
#cv.destroyAllWindows()