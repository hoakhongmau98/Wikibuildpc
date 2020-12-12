import os
import random as rm
import json


def getdata():
    dtc_product = []
    with open('app/static/Categories/Text/index.txt') as json_file:
        data = json.load(json_file)
        for p in data['product']:
            dtc = {}
            dtc['Name'] = p['Name']
            dtc['Content'] = p['Content']
            dtc['Link_direct'] = p['Link_direct']
            img_lst = os.listdir('app/static/Categories/img'+p['Link_direct']+'/')
            lst_img = rm.sample(img_lst, 8)
            dtc['Img'] = lst_img
            dtc_product.append(dtc)
    return dtc_product

