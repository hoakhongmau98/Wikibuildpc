from flask import Blueprint, render_template, url_for, redirect, flash, request
from .. import db
from .build_models import products
import pandas as pd
import time

build_blueprint = Blueprint('build', __name__)
lst_img = 0
lst_category = 0


@build_blueprint.route('/call_prodcut')
def product():
    global lst_img
    if lst_category ==0:
        lst_img = 0
    # arg == name table
    json = []
    pagenumber = 0
    direct = {}
    obj = request.args.get('call_arg')
    if ',' in obj:
        pagenumber = int(obj.split(',')[0])
        obj = obj.split(',')[1]
    # query all obj in obj = table
    obj_element = db.engine.execute('SELECT * FROM '+'element_' + obj).fetchall()
    count_page = len(obj_element)
    # get code from obj_elemant and filter by orm query
    if (pagenumber+1)*15 > count_page:
        print('over page')
        begin = (count_page//15)*15
        after = count_page
    else:
        begin = pagenumber*15
        after = pagenumber*15+15

    for i in range(begin, after):
        # print(i)
        code = obj_element[i].Code
        obj_product = products.query.filter_by(Code=code).first()
        linkimg = '/static/' + obj_product.img_directory
        name = obj_product.Name
        code = obj_product.Code
        price = obj_product.slase_price
        # print(len(price))
        if 3 < len(price) < 7:
            price = price[0:-3] + ',' + price[-3:] + ' đ'
        elif len(price) < 10:
            # print('here')
            price = price[0:-6] + ',' + price[-6:-3] + ',' + price[-3:] + ' đ'
        elif len(price) < 13:
            price = price[0:-9] + ',' + price[-9:-6] + ',' + price[-6:-3] + ',' + price[-3:] + ' đ'
        else:
            price = ''
        # return {'code': code, 'name': name, 'linkimg': linkimg, 'saleprice': price}
        # json.append(request(begin, after, obj_element))
        json.append({'code': code, 'name': name, 'linkimg': linkimg, 'saleprice': price})
    pageend = count_page // 15
    if pagenumber == pageend or pagenumber > pageend:
        pagenext = str(pageend) + ',' + obj
    else:
        pagenext = str(pagenumber+1) + ',' + obj

    if pagenumber == 0:
        pageprevious = obj
    pageprevious = str(pagenumber - 1) + ',' + obj
    direct = {'pageprevious': pageprevious, 'pagenext': pagenext, 'pagebegin': obj, 'pageend': str(pageend)+','+obj,
              'currentpagenumber': pagenumber, 'endpagenumber': pageend}
    # print(json['name'])
    # print(json['linkimg'])
    # print('first')
    # print('seconds')
    # print(json)
    obj_classify = db.engine.execute('SELECT * FROM '+'category_' + obj)
    return render_template("build/product.html", json_product=json, direct=direct)


@build_blueprint.route('/add_product')
def add_product():
    global lst_img
    lst_arg = request.args.get('call_add')
    obj_product = products.query.filter_by(Code=lst_arg).first()
    price = obj_product.slase_price
    # print(len(price))
    if 3 < len(price) < 7:
        price = price[0:-3] + ',' + price[-3:] + ' đ'
    elif len(price) < 10:
        # print('here')
        price = price[0:-6] + ',' + price[-6:-3] + ',' + price[-3:] + ' đ'
    elif len(price) < 13:
        price = price[0:-9] + ',' + price[-9:-6] + ',' + price[-6:-3] + ',' + price[-3:] + ' đ'
    else:
        price = ''
    choices = {'linkimg': obj_product.img_directory, 'price': price}
    lst_img += 1
    print(lst_img)
    return render_template("build/basket.html", choices=choices)


@build_blueprint.route('/categories')
def categories():
    global lst_category
    namecategory = request.args.get('call_arg')
    category = {}
    # print(namecategory)
    df = pd.read_sql_query('select * from category_'+namecategory, db.engine)
    # print(df)
    colname = df.columns
    # print(colname)
    for name in colname:
        data = df[name]
        check = df[name] != '- No Information'
        category[name] = list(data[check])
    lst_category = lst_category +1
    print(category)
    return render_template("build/categories.html", category=category)


# Đoạn mã sau chỉ được optimaze cho từng database <=> folder.csv
# not complete
# @build_blueprint.route('/updatedatabase')
# def updatedatabase():
#     product_Cpu = pd.read_csv('app/static/Categories/Product/product_Cpu.csv')
#     nametable = 'products'
#     querry = db.engine.execute('SELECT * FROM '+nametable).fetchall()
#     start_time = time.time()
#     # print(product_Cpu)
#     for row in range(len(product_Cpu)):
#         compare = (product_Cpu.iloc[row]['code'], product_Cpu.iloc[row]['name'], product_Cpu.iloc[row]['bao_hanh'],
#                    str(product_Cpu.iloc[row]['base_price']), str(product_Cpu.iloc[row]['slase_price']),
#                    product_Cpu.iloc[row]['img_directory'], product_Cpu.iloc[row]['infor_product'])
#         if compare in querry:
#             None
#             print('Here')
#         else:
#             print('False')
#             # objt = Product(product_Cpu.iloc[row]['code'], product_Cpu.iloc[row]['name'],
#             #                product_Cpu.iloc[row]['bao_hanh'],
#             #                str(product_Cpu.iloc[row]['base_price']), str(product_Cpu.iloc[row]['slase_price']),
#             #                product_Cpu.iloc[row]['img_directory'], product_Cpu.iloc[row]['infor_product'])
#             # db.session.add(objt)
#             # db.session.commit()
#             # print(objt)
#     # print(db.metadata.tables.keys())    # call name tables
#     print(f'Time run: {time.time()-start_time}')
#     print(querry)
#
#     return render_template('build/updatedatabase.html')
#
