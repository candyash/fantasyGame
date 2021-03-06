from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, IntegerField,PasswordField, RadioField
from flask_wtf.file import FileField
from wtforms.fields.html5 import DateField
from wtforms.validators import Optional, Length, Required, URL, Email, EqualTo
from flask.ext.pagedown.fields import PageDownField

class ProfileForm(Form):
    firstName=StringField('First Name', validators=[Required(),Length(1,30)])
    lastName=StringField('Last Name', validators=[Required(), Length(1,30)])
    submit=SubmitField('Submit')
class RegisterForm(Form):
    firstName=StringField('First Name', validators=[Required(),Length(1,30)] )
    lastName=StringField('Last Name', validators=[Required(),Length(1,30)] )
    country=StringField('Country', validators=[Required(),Length(1,30)] )
    city=StringField('City', validators=[Required(),Length(1,30)] )
    phoneNumber=IntegerField('Phone Number', validators=[Required()])
    username=StringField('Nick Name', validators=[Required()])
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])

    password = PasswordField('Password', [Required(), EqualTo('confirm')])
    confirm  = PasswordField('Confirm')
    submit = SubmitField('Register')

class CreatLeagueForm(Form):
    leagueName=StringField('League Name', validators=[Required(), Length(3,30)])
    photo_league = FileField('Picture upload')
    private = RadioField('private', choices=[('private','private'),('public','public')])
    gameType = RadioField('Game Type', choices=[('Seasonal','Seasonal'),('Keeper','Keeper')])
    matchType = RadioField('Match Type', choices=[('Classic Mode  (Rotisserie)','Classic Mode  (Rotisserie)'),('Head-to-head','Head-to-head')])
    champion = RadioField('Champion', choices=[('Play-offs','Play-offs'),('Head-to-head','Head-to-head')])
    submit=SubmitField('Create a League')
