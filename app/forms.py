 # -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(Form):
	uname = TextField('用户名', validators = [Required()])
	passwd = TextField('密码', validators = [Required()])
	remember_me = BooleanField('remember_me', default = False)

class CommentForm(Form):
	comment = TextField('内容', validators = [Required()])
	