 # -*- coding: utf-8 -*-
from app import db

class User(db.Model):
    uid = db.Column(db.Integer, primary_key = True, autoincrement = True)#用户唯一Uid
    name = db.Column(db.String(64), unique = True)#用户名
    passwd = db.Column(db.String(20))#用户密码，随机生成，也可以自行修改
    email = db.Column(db.String(120), unique = True)#用户邮箱地址，注册时发送确认邮件过去
    phone = db.Column(db.String(13), unique = True)#用户手机号，可以不填
    signature = db.Column(db.String(300))#用户签名
    avatarpath = db.Column(db.String(200))#用户头像
    timestamp = db.Column(db.DateTime)#创建时间
    #posts = db.relationship('Story', backref = 'author', lazy = 'dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.uid)

    def __repr__(self):
        return '<User %r>' % (self.name)

class Story(db.Model):
    sid = db.Column(db.Integer, primary_key = True)#故事唯一Sid
    summary = db.Column(db.String(140))#摘要
    target = db.Column(db.String(64))#对象，故事的B角
    target_email = db.Column(db.String(120))#对象邮箱地址
    timestamp = db.Column(db.DateTime)#投递时间
    storypath = db.Column(db.String(300))#故事的文件
    ower = db.Column(db.Integer, db.ForeignKey('user.uid'))#故事的A角

    def __repr__(self):
        return '<Story %r>' % (self.summary)

class Comment(db.Model):
    cid = db.Column(db.Integer, primary_key = True)#评论唯一cid
    comments = db.Column(db.String(1000))#评论内容
    tsid = db.Column(db.Integer, db.ForeignKey('story.sid'))#评论对象
    timestamp = db.Column(db.DateTime)#评论投递时间
    ower = db.Column(db.Integer, db.ForeignKey('user.uid'))#评论投递人

    def __repr__(self):
        return '<Story %r>' % (self.comments)