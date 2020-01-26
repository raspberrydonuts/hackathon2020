from flask import Flask, request, Response, render_template, redirect, flash, url_for
# import requests
# import itertools
# from flask_wtf.csrf import CSRFProtect
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# import wtforms
# from wtforms.validators import Regexp
# import re
# import json
# from flask_bootstrap import Bootstrap
# from models import LoginForm, SignupForm, ChampionForm, PlayerForm, SpellForm
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
def index():
   return redirect(url_for('index'))

