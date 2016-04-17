from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, IntegerField,PasswordField
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
