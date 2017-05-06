from wtforms import Form, StringField, BooleanField, PasswordField, validators


lich_lam = {
    'sangt2' : [],
    'chieut2' : [],
    'toit2' : [],
    'sangt3' : [],
    'chieut3' : [],
    'toit3' : [],
    'sangt4' : [],
    'chieut4' : [],
    'toit4' : [],
    'sangt5' : [],
    'chieut5' : [],
    'toit5' : [],
    'sangt6' : [],
    'chieut6' : [],
    'toit6' : [],
    'sangt7' : [],
    'chieut7' : [],
    'toit7' : [],
    'sangcn' : [],
    'chieucn' : [],
    'toicn' : []
};

class LichLamForm(Form):
    sangt2 = BooleanField('sangt2')
    chieut2 = BooleanField('chieut2')
    toit2 = BooleanField('toit2')
    sangt3 = BooleanField('sangt3')
    chieut3 = BooleanField('chieut3')
    toit3 = BooleanField('toit3')
    sangt4 = BooleanField('sangt4')
    chieut4 = BooleanField('chieut4')
    toit4 = BooleanField('toit4')
    sangt5 = BooleanField('sangt5')
    chieut5 = BooleanField('chieut5')
    toit5 = BooleanField('toit5')
    sangt6 = BooleanField('sangt6')
    chieut6 = BooleanField('chieut6')
    toit6 = BooleanField('toit6')
    sangt7 = BooleanField('sangt7')
    chieut7 = BooleanField('chieut7')
    toit7 = BooleanField('toit7')
    sangcn = BooleanField('sangcn')
    chieucn = BooleanField('chieucn')
    toicn = BooleanField('toicn')

class NhanVienForm(Form):
    ten = StringField('ten', [validators.data_required()] )
    matkhau = PasswordField('matkhau',[validators.data_required()])
