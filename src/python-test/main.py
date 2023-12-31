import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os
from classe import *

def path_test(path):
    assert path is not None, "file could not be read, check with os.path.exists()"

def convert_gray(img):
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return img_gray

def process(img_rgb, template, cont, img):
    img_gray = convert_gray(img_rgb)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.75
    loc = np.where( res >= threshold)
    coordenadas = []
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        cont+=1
        coordenadas.append((pt[0], pt[1]))
    coordenadas_str = ', '.join([f'({x}, {y})' for x, y in coordenadas])
    return img_rgb, cont, coordenadas_str

def sample_list(path):
    arquivos = [arq for arq in os.listdir(path) if os.path.isfile(os.path.join(path, arq))]
    print (arquivos)
    return arquivos

def main():
    path = './palhetas/'
    imgs = ['teste1.jpg', 'teste2.jpg', '20200214_143201.jpg']
    template_names = sample_list('./sample/')
    for template_name in template_names:
        for img in imgs:
            template = cv.imread('./sample/'+template_name, cv.IMREAD_GRAYSCALE)
            path_test(template)
            img_rgb = cv.imread(path+img)
            path_test(img_rgb)
            cont = 0
            img_rgb_proc, cont, coordinates = process(img_rgb, template, cont, img)
            if cont == 0: continue
            cv.imwrite('./results/media/'+img+'-'+f"template-{template_name}"+str(cont)+'.png',img_rgb_proc)
            export_data(img, cont, template_name, img, coordinates)

if __name__ == '__main__':
    main()
