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
    language = StringField('Language (DE,TR,ES,IT,RU,AR)', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Get me a random meal. Instructions in 2 languages!')

class BasriDiceForm(FlaskForm):
    dice1 = DecimalField('1: How many steps forward?', validators=[DataRequired()])
    dice2 = DecimalField('2: How many steps forward?', validators=[DataRequired()])
    dice3 = DecimalField('3: How many steps forward?', validators=[DataRequired()])
    dice4 = DecimalField('4: How many steps forward?', validators=[DataRequired()])
    dice5 = DecimalField('5: How many steps forward?', validators=[DataRequired()])
    dice6 = DecimalField('6: How many steps forward?', validators=[DataRequired()])
    submit = SubmitField('Show me!')
