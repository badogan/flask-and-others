from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class BasriForm(FlaskForm):
    var1 = StringField('Var1', validators=[DataRequired()])
    var2 = StringField('Var2', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')

class BasriForm2(FlaskForm):
    var1 = DecimalField('var1 in BasriForm2', validators=[DataRequired()])
    var2 = DecimalField('Var2 in BasriForm2', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Calculate')

class RandommealForm(FlaskForm):
    firstname = StringField('Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Get me a random meal!')
