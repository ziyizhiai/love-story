#!/usr/bin/python 
# -*- coding: utf-8 -*-
import sqlite3

db = sqlite3.connect("app.db")

#创建表
cur = db.cursor()

#用户表
cur.execute("drop table user")
cur.execute('''
CREATE TABLE user (
    uid INTEGER primary key autoincrement, 
    name VARCHAR(64), 
    passwd VARCHAR(20), 
    email VARCHAR(120), 
    phone VARCHAR(13), 
    signature VARCHAR(300), 
    avatarpath VARCHAR(200), 
    timestamp DATETIME, 
    UNIQUE (name), 
    UNIQUE (email), 
    UNIQUE (phone)
	);
''')

#故事表
cur.execute("drop table story")
cur.execute('''
CREATE TABLE story (
	sid INTEGER primary key autoincrement, 
    title VARCHAR(140),
	summary VARCHAR(140), 
	target VARCHAR(64), 
	target_email VARCHAR(120),  
	timestamp DATETIME, 
	storypath VARCHAR(300), 
	ower INTEGER,
	FOREIGN KEY(ower) REFERENCES user (uid)
);
''')

#评论表
cur.execute("drop table comment")
cur.execute('''
CREATE TABLE comment (
    cid INTEGER primary key autoincrement, 
    comments VARCHAR(1000), 
    tsid INTEGER, 
    timestamp DATETIME, 
    ower INTEGER, 
    FOREIGN KEY(tsid) REFERENCES story (sid), 
    FOREIGN KEY(ower) REFERENCES user (uid)
);
''')

#insert root story
#cur.execute("insert into user values ( 1, 'ziyizhiai', '7758258', 'ziyizhiai@gmail.com', '18664780153', '其实，我们都在追寻一种感动', '', datetime('now'))")
#cur.execute("insert into story values ( 1, '我们的爱', '分享你爱情，感受别人的爱情', 'janice', '273142579@qq.com', datetime('now'), '/opt/love-story/app/index', 1)")


db.commit()
db.close()