from flask import Flask, render_template, request, redirect, session, url_for, flash
from trashy import *
from mongodb import *
from nocache import nocache

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
@nocache
def main():
    note = None
    nv = NhanVienForm()
    if request.method == 'POST':
        nv = NhanVienForm(request.form)
        for nv_test in NhanVien.objects:
            if (nv.ten.data == nv_test.ten and nv.matkhau.data == nv_test.matkhau) and nv.validate():
                session['username'] = nv.ten.data
                return redirect('dangky')
            else:
                note = "Sai tên đăng nhập hoặc mật khẩu"
    return render_template('main.html',lichlam=lich_lam,form=nv,note=note)


@app.route('/dangky',methods=['GET','POST'])
@nocache
def dangky():
    if request.method == 'GET':
        form = LichLamForm()
        return render_template('dangky.html',form=form,lichlam = lich_lam, tennv = session['username'])
    else:
        form = LichLamForm(request.form)
        for buoi_lam in form:
            if str(buoi_lam.data) == "True":
                lich_lam[str(buoi_lam.name)].append(session['username'])
        return redirect('dangky')

@app.route('/xoa',methods=['GET','POST'])
@nocache
def xoa():
    if request.method == 'GET':
        form = LichLamForm()
        return render_template('xoa.html',form=form, lichlam= lich_lam, tennv= session['username'])
    else:
        form = LichLamForm(request.form)
        for buoi_lam in form:
            if str(buoi_lam.data) == "True":
                try: lich_lam[str(buoi_lam.name)].remove(session['username'])
                except ValueError:
                    pass
        return redirect('xoa')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('')

@app.route('/exec')
def exec():
    nv = NhanVien.objects.get(ten = 'Thành')
    nv.update(set__matkhau = 'thanh123')
    return 'Done'


@app.route('/doimatkhau',methods=['GET','POST'])
def doimatkhau():
    thanhcong = ''
    if request.method == 'POST':
        if request.form['matkhaumoi'] == request.form['matkhaumoi_xacnhan']:
            nhanvien = NhanVien.objects.get(ten = session['username'])
            nhanvien.update(set__matkhau = request.form['matkhaumoi'])
            thanhcong = 'Mật khẩu của bạn đã đổi thành "{0}" thành công'.format(request.form['matkhaumoi'])
        else:
            thanhcong = 'Sai mật khẩu xác nhận'
    return render_template('doimatkhau.html',tennv=session['username'],thanhcong=thanhcong)

app.secret_key = '43j1j29/z'
if __name__ == '__main__':
    app.run(port=5000)
