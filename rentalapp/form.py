from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,SelectField,TextAreaField
from wtforms import validators
from wtforms.fields.choices import RadioField, SelectField
from wtforms.validators import DataRequired, Email, Length
from wtforms.widgets.core import PasswordInput


class Signup(FlaskForm):
     firstname = StringField("Firstname: ", validators=[DataRequired()])
     lastname = StringField("Lastname: ", validators=[DataRequired()])
     state=StringField("State:",validators=[DataRequired()])
     matric=StringField("Matric number:",validators=[DataRequired()])
     number = StringField("Phone number: ", validators=[DataRequired(),Length(min=11)])
     mail = StringField("Email: ",validators=[Email()])
     sel=SelectField('Select',choices=[('sel','Student'),('sel','Lanlord')])
     username=StringField("Username: ",validators=[DataRequired()])
     password = PasswordField("Password ",validators=[PasswordInput()])
     address =TextAreaField("Address: ",validators=[DataRequired()])
     submit = SubmitField("Sign In")