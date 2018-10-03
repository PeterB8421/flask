"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template, flash
from .forms import LogUserForm, secti,masoform,UserForm,VyrobForm,GameUserForms
from ..data.database import db
from ..data.models import LogUser,GameUser
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

@blueprint.route('/gameuser', methods=['GET','POST'])
def gameuser():
    form=GameUserForms()
    if form.validate_on_submit():
        new_gameuser = GameUser.create(**form.data)
    return render_template('public/gameuser.tmpl',form=form)

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
