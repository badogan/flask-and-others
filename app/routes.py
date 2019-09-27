from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, BasriForm, BasriForm2, RandommealForm
import lib.BasriFunctions as h
import config as c

@app.route('/')
@app.route('/index')
def index():
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
    return render_template('index.html', title='Home', user=user, posts=posts)

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

@app.route('/randommeal', methods=['GET', 'POST'])
def randommeal():
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
        return redirect(url_for('index'))
    return render_template('InitiateRandommeal.html', title='Random Meal', form=form)

