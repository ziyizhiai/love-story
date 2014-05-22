#!/usr/bin/python 
# -*- coding: utf-8 -*-
import sqlite3

db = sqlite3.connect("app.db")
cur = db.cursor()
row = ('', 'abc', 'NOW()', '', '', )
cur.execute("delete from user")
cur.execute("insert into user values ( null, 'ziyizhiai', 'ziyizhiai', 'ziyizhiai@gmail.com', '18664780153', '', '', datetime('now') )")
cur.execute("select * from user")
print 'rows in user:'
for row in cur.fetchall(): print(row)

cur.execute("delete from story")
cur.execute("insert into story values ( null, '如果', '爱', 'ziyi', 'ziyi@gmail.com', datetime('now'), '', 1)")
cur.execute("select * from story")
print 'rows in story:'
for row in cur.fetchall(): print(row)

cur.execute("delete from comment")
cur.execute("insert into comment values ( null, '很棒', 1, datetime('now'), 1)")
cur.execute("select * from comment")
print 'rows in comment:'
for row in cur.fetchall(): print(row)
db.commit()
db.close()
#cur.execute("insert into comment values ( 1, 'abc', , ,)", row)