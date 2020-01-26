from flask import Flask, request, Response, render_template, redirect, flash, url_for
import requests
import itertools
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# import wtforms
# from wtforms.validators import Regexp
# import re
import json
# from flask_bootstrap import Bootstrap
# from models import LoginForm, SignupForm, ChampionForm, PlayerForm, SpellForm
# from flask_sqlalchemy import SQLAlchemy

csrf = CSRFProtect()
app = Flask(__name__)
csrf.init_app(app)


@app.route('/')
def default():
    if request.method == 'POST':
        # handle response from below render
        loc = request.values.get('location') # Your location 
        # if fetch location failed, redirect them to the form to enter
        # custom location
        redirect('/index?location='+loc)
    else:
        return render_template("fetch_location.html") # execute javascript with onload

@app.route('/index')
def index():
    return render_template("index.html")

