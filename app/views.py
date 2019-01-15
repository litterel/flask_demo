from flask import render_template, flash, redirect,url_for
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }]
    return render_template("index.html", title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # 登录页面
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me = {}'.format(form.username.data,form.remember_me.data))
        return url_for('index')
    return render_template('login.html', title='Sign In', form=form)
