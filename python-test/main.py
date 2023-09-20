import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from classe import *

def path_test(path):
    assert path is not None, "file could not be read, check with os.path.exists()"

def convert_gray(img):
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return img_gray

def pointers(pt):
    print('x: ', pt[0], 'y: ', pt[1])

def process(img_rgb, template, cont):
    img_gray = convert_gray(img_rgb)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        pointers(pt)
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        cont+=1
    cv.imwrite('res.png',img_rgb)
    return cont

def main():
    path = '../palhetas/'
    img = 'teste1.jpg'
    template_name = 'sample2.png'
    img_rgb = cv.imread(path+img)
    template = cv.imread('./sample/'+template_name, cv.IMREAD_GRAYSCALE)
    path_test(img_rgb)
    path_test(template)
    cont = 0
    cont = process(img_rgb, template, cont)
    export_data(img, cont, template_name)

if __name__ == '__main__':
    main()
