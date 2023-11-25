from flask import Flask, render_template, url_for, request, redirect, flash
from classes import Alban, Zereg, Tenhim, Mergejil, Bagsh, Oyutan

app = Flask(__name__)
app.secret_key = 'asas'

alban = Alban()
zereg = Zereg()
tenhim = Tenhim()
mergejil = Mergejil()
bagsh = Bagsh()
oyutan_ob = Oyutan()


@app.route('/')
def index():
    return render_template('index.html')


# Oyutan


@app.route('/oyutan/edit/<int:id>', methods=['GET', 'POST'])
def edit_oyutan(id):
    if request.method == 'GET':
        data = oyutan_ob.getRecord(id)
        tenhimData = tenhim.getRecords()
        return render_template('oyutan/edit.html', oyutan=data, tenhim=tenhimData)
    elif request.method == 'POST':
        scode = request.form['scode']
        sovog = request.form['sovog']
        sner = request.form['sner']
        gender = request.form['gender']
        elssen = request.form['elssen']
        register = request.form['register']
        tcode = request.form['tcode']
        simage = ''
        mcode = 0
        oyutan_ob.edit(id=id, scode=scode, sovog=sovog, sner=sner,
                       gender=gender, elssen=elssen, register=register, tcode=tcode, mcode=mcode, simage=simage)
        return redirect(url_for('list_oyutan'))


@app.route('/oyutan')
def list_oyutan():
    data = oyutan_ob.getRecords()
    return render_template('oyutan/list.html', oyutan=data)


@app.route('/oyutan/add', methods=['GET', 'POST'])
def add_oyutan():
    if request.method == 'GET':
        data = tenhim.getRecords()
        return render_template('oyutan/add.html', tenhim=data)
    elif request.method == 'POST':
        scode = request.form['scode']
        sovog = request.form['sovog']
        sner = request.form['sner']
        gender = request.form['gender']
        register = request.form['register']
        elssen = request.form['elssen']
        tcode = request.form['tcode']
        simage = ''
        mcode = 0
        oyutan_ob.add(scode=scode, sovog=sovog,         simage=simage,                  sner=sner,
                      gender=gender, elssen=elssen, tcode=tcode, mcode=mcode, register=register)
        return redirect(url_for('list_oyutan'))


@app.route('/oyutan/<int:id>')
def delete_oyutan(id):
    oyutan_ob.delete(id)
    return redirect(url_for('list_oyutan'))

# Bagsh


@app.route('/bagsh/edit/<int:id>', methods=['GET', 'POST'])
def edit_bagsh(id):
    if request.method == 'GET':
        data = bagsh.getRecord(id)
        tenhimData = tenhim.getRecords()
        return render_template('bagsh/edit.html', bagsh=data, tenhim=tenhimData)
    elif request.method == 'POST':
        bcode = request.form['bcode']
        bovog = request.form['bovog']
        bner = request.form['bner']
        gender = request.form['gender']
        aorson = request.form['aorson']
        tcode = request.form['tcode']
        atcode = 0
        ecode = 0
        bagsh.edit(id=id, bcode=bcode, bovog=bovog, bner=bner,
                   gender=gender, ajild_orson=aorson, tcode=tcode, atcode=atcode, ecode=ecode)
        return redirect(url_for('list_bagsh'))


@app.route('/bagsh/<int:id>')
def delete_bagsh(id):
    bagsh.delete(id)
    return redirect(url_for('list_bagsh'))


@app.route('/bagsh')
def list_bagsh():
    data = bagsh.getRecords()
    return render_template('bagsh/list.html', data=data)


@app.route('/bagsh/add', methods=['GET', 'POST'])
def add_bagsh():
    if request.method == 'GET':
        data = tenhim.getRecords()
        return render_template('bagsh/add.html', tenhim=data)
    elif request.method == 'POST':
        bcode = request.form['bcode']
        bovog = request.form['bovog']
        bner = request.form['bner']
        gender = request.form['gender']
        aorson = request.form['aorson']
        tcode = request.form['tcode']
        atcode = 0
        ecode = 0
        bagsh.add(bcode=bcode, bovog=bovog, bner=bner,
                  gender=gender, ajild_orson=aorson, tcode=tcode, atcode=atcode, ecode=ecode)
        return redirect(url_for('list_bagsh'))


# Mergejil


@app.route('/mergejil', methods=['GET', 'POST'])
def list_mergejil():
    if request.method == 'GET':
        datas = mergejil.getRecords()
        return render_template('mergejil/list.html', datas=datas)
    elif request.method == 'POST':
        aname = request.form['aname']
        mergejil.add(aname)
        return redirect(url_for('list_mergejil'))


@app.route('/mergejil/edit/<int:id>', methods=['GET', 'POST'])
def edit_mergejil(id):
    if request.method == 'GET':
        mergejilName = mergejil.getRecord(id)
        return render_template('mergejil/edit.html', aname=mergejilName)
    elif request.method == 'POST':
        aname = request.form['aname']
        mergejil.edit(id, aname)
        return redirect(url_for('list_mergejil'))


@app.route('/mergejil/delete/<int:id>')
def delete_mergejil(id):
    mergejil.delete(id)
    return redirect(url_for('list_mergejil'))


# Tenhim


@app.route('/tenhim', methods=['GET', 'POST'])
def list_tenhim():
    if request.method == 'GET':
        datas = tenhim.getRecords()
        return render_template('tenhim/list.html', datas=datas)
    elif request.method == 'POST':
        aname = request.form['aname']
        tenhim.add(aname)
        return redirect(url_for('list_tenhim'))


@app.route('/tenhim/edit/<int:id>', methods=['GET', 'POST'])
def edit_tenhim(id):
    if request.method == 'GET':
        tenhimName = tenhim.getRecord(id)
        return render_template('tenhim/edit.html', aname=tenhimName)
    elif request.method == 'POST':
        aname = request.form['aname']
        tenhim.edit(id, aname)
        return redirect(url_for('list_tenhim'))


@app.route('/tenhim/delete/<int:id>')
def delete_tenhim(id):
    tenhim.delete(id)
    return redirect(url_for('list_tenhim'))


# Zereg


@app.route('/zereg', methods=['GET', 'POST'])
def list_zereg():
    if request.method == 'GET':
        datas = zereg.getRecords()
        return render_template('zereg/list.html', datas=datas)
    elif request.method == 'POST':
        aname = request.form['aname']
        zereg.add(aname)
        return redirect(url_for('list_zereg'))


@app.route('/zereg/edit/<int:id>', methods=['GET', 'POST'])
def edit_zereg(id):
    if request.method == 'GET':
        zeregName = zereg.getRecord(id)
        return render_template('zereg/edit.html', aname=zeregName)
    elif request.method == 'POST':
        aname = request.form['aname']
        zereg.edit(id, aname)
        return redirect(url_for('list_zereg'))


@app.route('/zereg/delete/<int:id>')
def delete_zereg(id):
    zereg.delete(id)
    return redirect(url_for('list_zereg'))


# Alban


@app.route('/alban', methods=['GET', 'POST'])
def list_alban():
    if request.method == 'GET':
        datas = alban.getRecords()
        return render_template('alban/list.html', datas=datas)
    elif request.method == 'POST':
        aname = request.form['aname']
        alban.add(aname)
        return redirect(url_for('list_alban'))


@app.route('/alban/edit/<int:id>', methods=['GET', 'POST'])
def edit_alban(id):
    if request.method == 'GET':
        albanName = alban.getRecord(id)
        return render_template('alban/edit.html', aname=albanName)
    elif request.method == 'POST':
        aname = request.form['aname']
        alban.edit(id, aname)
        return redirect(url_for('list_alban'))


@app.route('/alban/delete/<int:id>')
def delete_alban(id):
    alban.delete(id)
    return redirect(url_for('list_alban'))


if __name__ == '__main__':
    app.run(debug=True)