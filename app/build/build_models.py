
from .. import db


# create db
class products(db.Model):
    __tablename__ = "products"

    Code = db.Column('Code', db.String(15), nullable=False, primary_key=True)
    Name = db.Column('Name', db.String(250), nullable=False)
    bao_hanh = db.Column('bao_hanh', db.TEXT(20), nullable=False)
    base_price = db.Column('base_price', db.TEXT(20), nullable=False)
    slase_price = db.Column('slase_price', db.String(15), nullable=False)
    img_directory = db.Column('img_directory', db.String(250), nullable=False)
    infor_product = db.Column('infor_product', db.String(50))

    def __init__(self, Code, Name, bao_hanh, base_price, slase_price, img_directory, infor_product):
        self.Code = Code
        self.Name = Name
        self.bao_hanh = bao_hanh
        self.base_price = base_price
        self.slase_price = slase_price
        self.img_directory = img_directory
        self.infor_product = infor_product
