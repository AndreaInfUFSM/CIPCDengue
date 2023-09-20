import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def path_test(path):
    assert path is not None, "file could not be read, check with os.path.exists()"

def convert_gray(img):
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return img_gray

def process(img_rgb, template):
    img_gray = convert_gray(img_rgb)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    cv.imwrite('res.png',img_rgb)

def main():
    templates = ['./sample/sample1.png', './sample/sample2.png', './sample/sample3.png']
    img_rgb = cv.imread('../palhetas/teste2.jpg')
    template = cv.imread('./sample/sample3.png', cv.IMREAD_GRAYSCALE)
    path_test(img_rgb)
    path_test(template)
    process(img_rgb, template)

if __name__ == '__main__':
    main()
