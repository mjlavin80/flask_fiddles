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



"""
1. object oriented
2. one for documents ... 'SELECT doc_id, title, authorship, role FROM metadata'
3. one for corpora
4. one for a single document view ... a way to preview/expand/export basic test results, tokens, POS, counts, eventually sentiment scores first 100 from tokens, top 25 from counts
5. one for a single corpus view ... each member links to single doc view
*
SELECT corpus_id, corpus_title, GROUP_CONCAT(joiner.doc_id) AS doc_id, GROUP_CONCAT(title) AS titles, GROUP_CONCAT(authorship) AS authors, GROUP_CONCAT(role SEPARATOR ', ') AS roles FROM 
((SELECT corpus_doc.corpus_id AS corpus_id, corpus_title, doc_id FROM corpus_doc LEFT JOIN corpus ON corpus.corpus_id=corpus_doc.corpus_id ORDER BY corpus_id) AS joiner)
LEFT JOIN metadata ON joiner.doc_id=metadata.doc_id GROUP BY corpus_id;


OLD: 
SELECT corpus_id, corpus_title, joiner.doc_id AS doc_id, title, authorship, role FROM 
((SELECT corpus_doc.corpus_id AS corpus_id, corpus_title, doc_id FROM corpus_doc LEFT JOIN corpus ON corpus.corpus_id=corpus_doc.corpus_id ORDER BY corpus_id) AS joiner)
LEFT JOIN metadata ON joiner.doc_id=metadata.doc_id;
"""

SELECT `COLUMN_NAME` 
FROM `INFORMATION_SCHEMA`.`COLUMNS` 
WHERE `TABLE_SCHEMA`='py_style' 
    AND `TABLE_NAME`='metadata';