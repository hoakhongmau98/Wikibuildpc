from build_models import Product
from .. import db
import pandas as pd


conn = db.engine

# product dataframe
product_Cpu = pd.read_csv('../static/Categories/Product/product_Cpu.csv')
product_Case = pd.read_csv('../static/Categories/Product/product_Case.csv')
product_Fan = pd.read_csv('../static/Categories/Product/product_Fan.csv')
product_Hdd = pd.read_csv('../static/Categories/Product/product_Hdd.csv')
product_Keyboard = pd.read_csv('../static/Categories/Product/product_Keyboard.csv')
product_Main = pd.read_csv('../static/Categories/Product/product_Main.csv')
product_Mouse = pd.read_csv('../static/Categories/Product/product_Mouse.csv')
product_Monitor = pd.read_csv('../static/Categories/Product/product_Monitor.csv')
product_Psu = pd.read_csv('../static/Categories/Product/product_Psu.csv')
product_Ram = pd.read_csv('../static/Categories/Product/product_Ram.csv')
product_Ssd = pd.read_csv('../static/Categories/Product/product_Ssd.csv')
product_Vga = pd.read_csv('../static/Categories/Product/product_Vga.csv')


# Element
element_Cpu = pd.read_csv('../static/Categories/Element/element_Cpu.csv')
element_Case = pd.read_csv('../static/Categories/Element/element_Case.csv')
element_Fan = pd.read_csv('../static/Categories/Element/element_Fan.csv')
element_Hdd = pd.read_csv('../static/Categories/Element/element_Hdd.csv')
element_Keyboard = pd.read_csv('../static/Categories/Element/element_Keyboard.csv')
element_Main = pd.read_csv('../static/Categories/Element/element_Main.csv')
element_Mouse = pd.read_csv('../static/Categories/Element/element_Mouse.csv')
element_Monitor = pd.read_csv('../static/Categories/Element/element_Monitor.csv')
element_Psu = pd.read_csv('../static/Categories/Element/element_Psu.csv')
element_Ram = pd.read_csv('../static/Categories/Element/element_Ram.csv')
element_Ssd = pd.read_csv('../static/Categories/Element/element_Ssd.csv')
element_Vga = pd.read_csv('../static/Categories/Element/element_Vga.csv')


# Category_Classiify
category_Cpu = pd.read_csv('../static/Categories/Category_classify/category_Cpu.csv')
category_Case = pd.read_csv('../static/Categories/Category_classify/category_Case.csv')
category_Fan = pd.read_csv('../static/Categories/Category_classify/category_Fan.csv')
category_Hdd = pd.read_csv('../static/Categories/Category_classify/category_Hdd.csv')
category_Keyboard = pd.read_csv('../static/Categories/Category_classify/category_Keyboard.csv')
category_Main = pd.read_csv('../static/Categories/Category_classify/category_Main.csv')
category_Mouse = pd.read_csv('../static/Categories/Category_classify/category_Mouse.csv')
category_Monitor = pd.read_csv('../static/Categories/Category_classify/category_Monitor.csv')
category_Psu = pd.read_csv('../static/Categories/Category_classify/category_Psu.csv')
category_Ram = pd.read_csv('../static/Categories/Category_classify/category_Ram.csv')
category_Ssd = pd.read_csv('../static/Categories/Category_classify/category_Ssd.csv')
category_Vga = pd.read_csv('../static/Categories/Category_classify/category_Vga.csv')


# defind name of product dataframe
product_dataframe = [product_Case, product_Cpu, product_Fan, product_Hdd, product_Keyboard,
                     product_Main, product_Mouse, product_Monitor, product_Psu, product_Ram,
                     product_Ssd, product_Vga]

element_dataframe = [element_Case, element_Cpu, element_Fan, element_Hdd, element_Keyboard,
                     element_Main, element_Mouse, element_Monitor, element_Psu, element_Ram,
                     element_Ssd, element_Vga]

element_dataframe_name = ['element_Case', 'element_Cpu', 'element_Fan', 'element_Hdd', 'element_Keyboard',
                          'element_Main', 'element_Mouse', 'element_Monitor', 'element_Psu', 'element_Ram',
                          'element_Ssd', 'element_Vga']

category_dataframe = [category_Case, category_Cpu, category_Fan, category_Hdd,
                      category_Keyboard, category_Main, category_Mouse, category_Monitor,
                      category_Psu, category_Ram, category_Ssd, category_Vga]

category_dataframe_name = ['category_Case', 'category_Cpu', 'category_Fan', 'category_Hdd',
                           'category_Keyboard', 'category_Main', 'category_Mouse', 'category_Monitor',
                           'category_Psu', 'category_Ram', 'category_Ssd', 'category_Vga']


def insertproduct():
    # insert dataframe to Product table
    for dataframe in product_dataframe:
        for row in range(len(dataframe)):
            objt = Product(dataframe.iloc[row]['code'], dataframe.iloc[row]['name'], dataframe.iloc[row]['bao_hanh'],
                           str(dataframe.iloc[row]['base_price']), str(dataframe.iloc[row]['slase_price']),
                           dataframe.iloc[row]['img_directory'], dataframe.iloc[row]['infor_product'])
            db.session.add(objt)
            db.session.commit()


def insertelement():
    # insert dataframe to each table vs it name
    for item in range(len(element_dataframe)):
        print(element_dataframe[item].keys())
        print(item)
        print(element_dataframe_name[item])
        element_dataframe[item].to_sql(name=element_dataframe_name[item], con=db.engine, index=False)



def insertcategory_table():
    # insert dataframe to each table vs it name
    for item in range(len(category_dataframe)):
        print(category_dataframe[item])
        print(category_dataframe_name[item])
        category_dataframe[item].to_sql(name=category_dataframe_name[item], con=db.engine, index=False)


insertproduct()
insertelement()
insertcategory_table()

