from flask import Flask, jsonify, render_template, url_for, redirect
import jinja2
from flask_sql import app
from flaskext.mysql import MySQL

"""cursor.execute("SELECT first, last from people")
self.columns = [u'first', u'last']
a['first'] = "<a href=/people/"+a['first']+">"+a['first']+"</a>"
"""
#DB Connect ...
mysql = MySQL()
db_configs = {'MYSQL_DATABASE_USER':'root', 'MYSQL_DATABASE_PASSWORD': 'wyoming99', 'MYSQL_DATABASE_DB': 'py_style', 'MYSQL_DATABASE_HOST': 'localhost'}
for i, j in db_configs.items():
    app.config[i] = j
mysql.init_app(app)
#self.conn = mysql.connect()
cursor = mysql.connect().cursor()

class Table(object):
	def __init__(self, query, columns, cursor):
		self.query = query
		self.columns = columns
		self.cursor = cursor 
		self.data_dicts = [] #list of dictionaries, each dict is a key value pair
		self.do_query()

	def do_query(self):
		self.cursor.execute(self.query)
		data = self.cursor.fetchall()
		for i in data:
		    strings = [unicode(j).encode('utf8') for j in i]
		    a = dict(zip(self.columns, i))
		    self.data_dicts.append(a)

documents_table = Table(query='SELECT doc_id, title, authorship, role FROM metadata', columns = ['doc_id', 'title', 'authorship', 'role'], cursor=cursor)

corpus_query = 'SELECT corpus_id, corpus_title, GROUP_CONCAT(joiner.doc_id) AS doc_ids, GROUP_CONCAT(title) AS titles, GROUP_CONCAT(authorship) AS authors, GROUP_CONCAT(role SEPARATOR \', \') AS roles FROM\
((SELECT corpus_doc.corpus_id AS corpus_id, corpus_title, doc_id FROM corpus_doc LEFT JOIN corpus ON corpus.corpus_id=corpus_doc.corpus_id ORDER BY corpus_id) AS joiner)\
LEFT JOIN metadata ON joiner.doc_id=metadata.doc_id GROUP BY corpus_id;'

corpus_table = Table(query=corpus_query, columns = ['corpus_id', 'corpus_title', 'doc_ids', 'titles', 'authors', 'roles'], cursor=cursor)


"""
1. object oriented
2. one for documents ... 'SELECT doc_id, title, authorship, role FROM metadata'
3. one for corpora
4. one for a single document view ... a way to preview/expand/export basic test results, tokens, POS, counts, eventually sentiment scores first 100 from tokens, top 25 from counts
5. one for a single corpus view ... each member links to single doc view
*



OLD: 
SELECT corpus_id, corpus_title, joiner.doc_id AS doc_id, title, authorship, role FROM 
((SELECT corpus_doc.corpus_id AS corpus_id, corpus_title, doc_id FROM corpus_doc LEFT JOIN corpus ON corpus.corpus_id=corpus_doc.corpus_id ORDER BY corpus_id) AS joiner)
LEFT JOIN metadata ON joiner.doc_id=metadata.doc_id;
"""

"""
SELECT `COLUMN_NAME` 
FROM `INFORMATION_SCHEMA`.`COLUMNS` 
WHERE `TABLE_SCHEMA`='py_style' 
    AND `TABLE_NAME`='metadata';
    """