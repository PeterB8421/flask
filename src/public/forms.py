import re

from flask_wtf import Form
from wtforms.fields import BooleanField, TextField, PasswordField, DateTimeField, IntegerField,SelectField,DateField,FloatField
from wtforms.validators import EqualTo, Email, InputRequired, Length

from ..data.models import User, LogUser
from ..fields import Predicate

def email_is_available(email):
    if not email:
        return True
    return not User.find_by_email(email)

def username_is_available(username):
    if not username:
        return True
    return not User.find_by_username(username)

def safe_characters(s):
    " Only letters (a-z) and  numbers are allowed for usernames and passwords. Based off Google username validator "
    if not s:
        return True
    return re.match(r'^[\w]+$', s) is not None


def safe_street_characters(s):
    " Only letters (a-z) and  numbers are allowed for usernames and passwords. Based off Google username validator "
    if not s:
        return True
    return re.match(r'^(.*[^0-9]+) (([1-9][0-9]*)/)?([1-9][0-9]*[a-cA-C]?)$', s) is not None


def safe_city_characters(s):
    " Only letters (a-z) and  numbers are allowed for usernames and passwords. Based off Google username validator "
    if not s:
        return True
    return re.match(r'^\w{1,}$', s) is not None


def safe_postcode_characters(s):
    " Only letters (a-z) and  numbers are allowed for usernames and passwords. Based off Google username validator "
    if not s:
        return True
    return re.match(r'^\d{5}$', s) is not None

def safe_dph(s):
    if s == 21:
        return True
    elif s == 15:
        return True
    elif s == 10:
        return True
    return False


class LogUserForm(Form):

    jmeno = TextField('Choose your username', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=6, max=30, message="Please use between 6 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    prijmeni = TextField('Choose your username', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=6, max=30, message="Please use between 6 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    pohlavi = BooleanField('Pohlavi')


class secti(Form):
    hodnota1 = IntegerField("vlozHodnotu1", validators=[InputRequired(message="vyzadovano")])
    hodnota2 = IntegerField("vlozHodnotu2", validators=[InputRequired(message="vyzadovano")])


class masoform(Form):
    typ=SelectField('Typ', choices=[(1, "Hovezi"), (2, "Veprove")], default=2)


class UserForm(Form):
    jmeno = TextField('First name', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=3, max=30, message="Please use between 3 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    prijmeni = TextField('Last name', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=3, max=40, message="Please use between 3 and 40 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    datumNarozeni = DateField('Birtdate')
    ulice = TextField('Street', validators=[
        Predicate(safe_street_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=3, max=50, message="Please use between 3 and 50 characters"),
        InputRequired(message="You can't leave this empty")
                      ])
    mesto = TextField('City',validators=[
        Predicate(safe_city_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=2, max=40, message="Please use between 2 and 40 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    psc = TextField('Postcode',validators=[
        Predicate(safe_postcode_characters, message="Please use only numbers without whitespace characters."),
        Length(min=5, max=5, message="Please use only 5 characters"),
        InputRequired(message="You can't leave this empty")
    ])

class VyrobForm(Form):
    vyrobek = TextField("Vyrobek", validators=[
        Predicate(safe_characters,message="Pouzijte pouze pismena (a-z), bez ceskych znaku!"),
        Length(min=1,max=30, message="Zadejte maximalne 30 znaku."),
        InputRequired(message="Toto pole nesmi byt prazdne!")
    ])
    ks = IntegerField("Kusu",validators=[
        InputRequired(message="Toto pole nesmi byt prazdne!")
    ])
    cena = FloatField("Cena",validators=[
        InputRequired(message="Toto pole nesmi byt prazdne!")
    ])
    dph = IntegerField("DPH v %",validators=[
        Predicate(safe_dph, message="DPH muze byt pouze 10, 15 nebo 21 %!"),
        InputRequired(message="Toto pole nesmi byt prazdne!")
    ])

class GameUserForms(Form):
        username = TextField('Username', validators=[
            Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
            Length(min=3, max=30, message="Please use between 3 and 30 characters"),
            InputRequired(message="You can't leave this empty")
        ])
        email = TextField('Email', validators=[
            Length(min=3, max=40, message="Please use between 3 and 40 characters"),
            InputRequired(message="You can't leave this empty")
        ])
        date = DateField('Date')

