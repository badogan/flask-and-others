from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, BasriForm, BasriForm2, RandommealForm, BasriDiceForm, BasriSuggestionsForm
from app.models import Suggestion
import lib.BasriFunctions as h
import config as c
import numpy as np
import base64
from io import BytesIO
from matplotlib.figure import Figure
import pandas as pd

@app.route('/')
@app.route('/index')
def index():
    '''
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    =======index.html======
    {% block content %}
    <h1>Hi, {{ user.username }}!</h1>
    {% for post in posts %}
    <div><p>{{ post.author.username }} says: <b>{{ post.body }}</b></p></div>
    {% endfor %}
    {% endblock %}
    =======return as!!!======
    return render_template('index.html', title='Home', user=user, posts=posts)
    '''
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/basri', methods=['GET', 'POST'])
def basri():
    form = BasriForm()
    if form.validate_on_submit():
        flash('Var1 for user {}, Var2 for user {}, remember_me={}'.format(
            form.var1.data, form.var2.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('getdata.html', title='Basri', form=form)

@app.route('/basri2', methods=['GET', 'POST'])
def basri2():
    form = BasriForm2()
    if form.validate_on_submit():
        multiplied_value = h.BasriNumbers(form.var1.data,form.var2.data).MultiplyThem()
        flash('Var1 for user: {}, |Var2 for user: {}, |multiplication {}, |SECRET_KEY: {}, |USERNAME:{}'.format(
            form.var1.data, form.var2.data, multiplied_value, c.Config.SECRET_KEY,c.Config.USERNAME))
        return redirect(url_for('index'))
    return render_template('getdata2.html', title='Basri', form=form)

@app.route('/suggestions', methods=['GET', 'POST'])
def suggestions():
    user = {'username': 'Basri'}                     
    posts = [
        {
            'body': 'Gets your suggestions. List previous suggestions'
        },
        {
            'body': 'To demonstate basic database operations.'
        },
        {
            'body': 'SQLAlchemy, AWS RDS (MySQL)'
        }
    ]
            
    form = BasriSuggestionsForm()
    if form.validate_on_submit():
        flash('Others have provided the following so far...')
        suggestions_retreived_from_db = Suggestion.query.all()
        for s in suggestions_retreived_from_db:
            flash(s)
        flash('Your suggestions: {}'.format(form.Suggestions.data))
        suggestion = Suggestion(body=form.Suggestions.data)
        db.session.add(suggestion)
        db.session.commit()
        return render_template('index_Suggestions.html', title='Home', user=user, posts=posts)
    return render_template('suggestions.html', title='Basri Suggestions', form=form)

@app.route('/dice', methods=['GET', 'POST'])
def dice():
    user = {'username': 'Basri'}                     
    posts = [
        {
            'body': 'An imaginary and random dice is thrown. :)'
        },
        {
            'body': 'Next move is assessed according to the table you entered in the previous form.'
        },
        {
            'body': 'Process is repeated until the total value reaches to 100'
        },
        {
            'body': 'Maximum 2000 dice throws allowed!'
        }
    ]
    form = BasriDiceForm()
    if form.validate_on_submit():
        flash('Dice1: {},|Dice2: {},|Dice3: {},|Dice4: {},|Dice5: {},|Dice6: {}'.format(
            form.dice1.data,form.dice2.data,form.dice3.data,form.dice4.data,form.dice5.data,form.dice6.data))
        url_to_pass = h.BasriDiceAPICall(form.dice1.data,
                                         form.dice2.data,
                                         form.dice3.data,
                                         form.dice4.data,
                                         form.dice5.data,
                                         form.dice6.data
                                         ).CreateFigure()
        return render_template('index_dice.html', title='Home', user=user, posts=posts, name = 'new_plot_from_the_real_code', url=url_to_pass)
    return render_template('dice.html', title='Basri Dice', form=form)

@app.route('/randommeal', methods=['GET', 'POST'])
def randommeal():
    user = {'username': 'Basri'}                     
    posts = [
        {
            'body': 'A random meal is brought to you from:'
        },
        {
            'body': 'a site who provides such service through an API call'
        },
        {
            'body': 'The instruction received is passed to AWS Translate service so that you also receive it in the lanaguage you asked for!'
        },
        {
            'body': 'Example for amalgamation of services in the new world :)'
        }
    ]
    form = RandommealForm()
    if form.validate_on_submit():
        url = 'https://www.themealdb.com/api/json/v1/1/random.php'
        received_data = h.BasriAPICall(url).GetJSONData()        
        flash('Name of meal: {}'.format(received_data['meals'][0]['strMeal']))
        flash('Image of meal: {}'.format(received_data['meals'][0]['strMealThumb']))
        flash('Source of meal: {}'.format(received_data['meals'][0]['strSource']))
        flash('YouTube Link of meal: {}'.format(received_data['meals'][0]['strYoutube']))
        flash('Ingredients:')
        reduced_df = h.BasriAPICallReduceDF(received_data).ReduceDF()
        var=0
        while var < len(reduced_df):
            for key,value in reduced_df[var].items():
                flash('{},{}'.format(key, value))
            var=var+1
        flash('Instructions: {}'.format(received_data['meals'][0]['strInstructions']))
        temp = h.BasriAPITranslate(received_data['meals'][0]['strInstructions'],str(form.language.data)).Translate()
        flash('Instructions in {}: {}'.format(form.language.data,temp))
        #return redirect(url_for('index'))
        return render_template('index_Randommeal.html', title='Home', user=user, posts=posts, name = 'dnm name')
    return render_template('InitiateRandommeal.html', title='Random Meal', form=form)
