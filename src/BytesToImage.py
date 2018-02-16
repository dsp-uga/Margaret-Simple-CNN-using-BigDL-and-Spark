import numpy as np
import requests
import cv2
import os


def convert_to_img(file):
    counterx = 0
    x = []
    temp = []
    file = file.strip("\n")
    path = 'https://storage.googleapis.com/uga-dsp/project2/data/bytes/'+file+'.bytes'
    source_code = requests.get(path)
    plain_text = source_code.text
    #print plain_text
    lines = plain_text.split("\n")
    for line in lines:
        counterx = counterx + 1
        values = line.split(" ")
        values = values[1:]
        flag = 0
        for j in range(0, len(values)):
            if (values[j] == "??" or values[j] == "??\r\n"):
                flag = 1
                break
            values[j] = int(values[j], 16)
            if (flag == 0):
                temp = temp + values
            if (len(temp) == 16):
                x.append(temp)
                temp = []

    x = np.array(x)
    return x
