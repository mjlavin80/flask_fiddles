from flask import Flask, jsonify, render_template, url_for, redirect
import jinja2
from flask_sql import app
from flaskext.mysql import MySQL

from sql import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/people/')
@app.route('/people/<person>')
def people(person='nobody'):
    return 'A page just for ' + person

@app.route('/learn/')
def learn():
    return render_template('learn.html')

@app.route('/browse/')
def browse():
    return render_template('browse.html')

@app.route('/analyze/')
def analyze():
    return render_template('analyze.html')

@app.route('/manage/')
def manage():
    return render_template('manage.html')

@app.route('/home/')
def home():
    return redirect(url_for('.index'))

@app.route('/documents-data/')
def data():
    return jsonify(data=l_dicts)

