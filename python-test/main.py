import cv2 as cv
import numpy as np
import json
from matplotlib import pyplot as plt

class ImageInfo:
    def __init__(self, name, x_pos, y_pos, count, template_name):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.count = count
        self.template_name = template_name

    def __str__(self):
        return "name: " + self.name + "\nwidth: " + str(self.x_pos) + "\nheight: " + str(self.y_pos) + "\nchannels: " + str(self.count) + "\ntemplate_name: " + self.template_name

    def __repr__(self):
        return "name: " + self.name + "\nwidth: " + str(self.x_pos) + "\nheight: " + str(self.y_pos) + "\nchannels: " + str(self.count) + "\ntemplate_name: " + self.template_name

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

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

def export_data(img, cont, template_name):
    image_info = ImageInfo(img,25,30,cont, template_name)
    json_str = image_info.to_json()
    json_file_name = "image_info.json"
    with open(json_file_name, "w") as json_file:
        json_file.write(json_str)

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
