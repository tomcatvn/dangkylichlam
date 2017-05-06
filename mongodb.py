from mongoengine import *

connect(db = 'rome_coffee',
        username = 'thanh',
        password = '-thanh',
        host = 'ds127531.mlab.com',
        port = 27531
        )

class NhanVien(Document):
    ten = StringField()
    matkhau = StringField()




