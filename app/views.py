#!/usr/bin/python 
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import sqlite3
from flask import render_template, flash, redirect, session, url_for, request, g 
#from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, DATABASE, STORYDIR

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db



@app.teardown_appcontext
def close_connection(exception):
	if db:db.close()



@app.route('/hello', methods=['GET'])
@app.route('/', methods=['GET'])
def gHome():
    return render_template('index.html')



@app.route('/ours', methods=['GET'])
def gOurs():
	return render_template('ours.html')
@app.route('/ours', methods=['POST'])
def pOurs():
	title=request.form['mce_0']
	story=request.form['mce_1']
	db = get_db()
	cur = db.cursor()
	cur.execute("select max(sid) from story")
	id = cur.fetchone()[0]
	if not id: id = 0
	id = id + 1
	cur.execute("insert into story values ( null, ?, '', ?, '', datetime('now'), '', ?)", (title,'', 0))
	db.commit()
	f = open(STORYDIR + str(id), 'w')
	f.write(story)
	f.close()
	# db.commit()
	# cur.execute("select * from comment")
	# result = ''
	# for row in cur.fetchall(): 
	# 	result = result + '\n' + row[1]
	# flash(result)
	return redirect('/theirs')
	

@app.route('/theirs', methods=['GET'])
def gTheirs():
	story = {}
	db = get_db()
	cur = db.cursor()
	cur.execute("select max(sid) from story")
	id = cur.fetchone()[0]
	if not id: return render_template('theirs.html')
	f = open(STORYDIR + str(id), 'r')
	story['content'] = f.read()
	f.close()
	cur.execute("select title from story where sid=?", (id,))
	title = cur.fetchone()[0]
	story['title'] = title
	return render_template('theirs.html', story = story)



@app.route('/contact', methods=['GET'])
def gContact():
	return render_template('contact.html')



@app.route('/user', methods=['GET'])
def gUser():
	return render_template('user.html')



@app.route('/comment', methods=['GET'])
def gComment():
	return render_template('comment.html')


@app.route('/comment', methods=['POST'])
def pComment():
	name = request.form['name']
	email = request.form['email']
	message = request.form['message']
	db = get_db()
	cur = db.cursor()
	cur.execute("insert into comment values ( null, ?, ?, datetime('now'), ?)", (message, 1, 1))
	db.commit()
	cur.execute("select * from comment")
	result = ''
	for row in cur.fetchall(): 
		result = result + '\n' + row[1]
	flash(result)
	return redirect('/')