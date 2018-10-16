"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template, flash
from .forms import LogUserForm, secti,masoform,UserForm,VyrobForm,GameUserForms,GameUserForms_Edit, Deti_Form
from ..data.database import db
from ..data.models import LogUser,Deti
from datetime import datetime
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/tabulka', methods=['GET','POST'])
def tabulka():
    form=UserForm()
    pole1=[[1,"text"],[2,"text2"]]
    if form.validate_on_submit():
        print(form.jmeno.data)
    return render_template('public/tabulka.tmpl',pole1=pole1,form=form)

@blueprint.route('/vyrobky', methods=['GET','POST'])
def vyrobky():
    form=VyrobForm()
    if form.validate_on_submit():
        return render_template('public/vyrobky_vysledek.tmpl', form=form, cena=form.cena.data, vyrobek=form.vyrobek.data, ks=form.ks.data, dph=form.dph.data,suma=form.cena.data*form.ks.data*(float(form.dph.data)/100+1))
    return render_template('public/vyrobky.tmpl',form=form)
@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/secti', methods=['GET','POST'])
def scitani():
    form = secti()
    if form.validate_on_submit():
        return render_template('public/vystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/secti.tmpl', form=form)

@blueprint.route('/maso', methods=['GET','POST'])
def masof():
    form = masoform()
    if form.validate_on_submit():
        return render_template('public/masovystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/maso.tmpl', form=form)

@blueprint.route("/deti",methods=["GET","POST"])
def deti_view():
    form = Deti_Form()
    if form.validate_on_submit():
        new_deti = Deti.create(**form.data)
        flash(message="Vytvoren zaznam.",category="warning")
        return render_template("public/deti.tmpl",form=form)
    return render_template("public/deti.tmpl",form=form)

@blueprint.route("/deti/<int:id>",methods=["GET","POST"])
def deti_edit(id):
    user = db.session.query(Deti).get(id)
    form = Deti_Form(obj = user)
    if form.validate_on_submit():
        edit_deti = user.update(**form.data)
        flash("Uspesne zmeneno.",category="info")
    return render_template("public/deti.tmpl",form=form)

@blueprint.route("/deti/<int:id>/remove",methods=["GET","POST"])
def deti_delete(id):
    user = db.session.query(Deti).get(id)
    form = Deti_Form(obj = user)
    if form.validate_on_submit():
        delete_deti = user.delete(id)
        flash("Uspesne smazano.",category="info")
    return render_template("public/deti_smazat.tmpl",form=form)
