import os
import random as rm
import json


def getimg(keyword):
    img_lst = os.listdir('app/static/Categories/img' + '/' + keyword + '/')
    lst_img = rm.sample(img_lst, 12)
    lst_img = [keyword + '/' + link for link in lst_img]
    return lst_img

