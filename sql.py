from flask import Flask, jsonify, render_template, url_for, redirect
import jinja2
from flask_sql import app
from flaskext.mysql import MySQL

mysql = MySQL()

db_configs = {'MYSQL_DATABASE_USER':'root', 'MYSQL_DATABASE_PASSWORD': 'wyoming99', 'MYSQL_DATABASE_DB': 'matt', 'MYSQL_DATABASE_HOST': 'localhost'}

for i, j in db_configs.items():
    app.config[i] = j

mysql.init_app(app)
#print app.config

conn = mysql.connect()
cursor = mysql.connect().cursor()

cursor.execute("SELECT first, last from people")
data = cursor.fetchall()

l_dicts = []
h = [u'first', u'last']
for i in data:
    strings = [j.encode('utf8') for j in i]
    a = dict(zip(h, i))
    a['first'] = "<a href=/people/"+a['first']+">"+a['first']+"</a>"
    l_dicts.append(a)