import base64
import jwt
import os
from app import db
from datetime import datetime, timedelta
from flask import url_for, current_app
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'User'
    username = db.Column(db.String(64), primary_key=True, index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))  # 不保存原始密码
    name = db.Column(db.String(64))
    about_me = db.Column(db.String(128))

    # 在打印的时候更好看，不会愚蠢的输出类的信息
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    #todict和fromdict主要用于前后端交互，它们之间传递的是JSON对象。
    def to_dict(self, include_email=False):
        data = {
            'username': self.username,
            'name': self.name,
            'about_me': self.about_me,
        }

        if include_email:
            data['email'] = self.email
        return data

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])

    def get_jwt(self, expires_in=600):
        now = datetime.utcnow()
        # 将用户id和名称等信息作为payload加入token中
        payload = {
            'username': self.username,
            'name': self.name if self.name else self.username,
            'exp': now + timedelta(seconds=expires_in),
            'iat': now
        }
        # 使用jwt的加密算法进行加密
        return jwt.encode(
            payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_jwt(token):
        try:
            # 进行解密验证
            payload = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256'])
            # 如果token过期那么就验证失败，否则就返回id
        except jwt.exceptions.ExpiredSignatureError as e:
            return None
        # return payload
        return User.query.get(payload.get('username'))


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)  # 博客id
    title = db.Column(db.String(255),index=True)  # 标题
    loc = db.Column(db.String(255))  # 博客路径/所在文件夹。 因为我在本地写博客喜欢文件夹分类，传入的是总路径，所以还需要把次级路径传进去
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 时间戳
    views = db.Column(db.Integer, default=0)  # 多少人看过该文章
    def __repr__(self):
        return '<Blog {}>'.format(self.title)


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    tagname = db.Column(db.String(255))
    # 外键，关联博客
    blogId = db.Column(db.ForeignKey('Blog.id'))


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(128))
    email = db.Column(db.String(128))
    comment = db.Column(db.Text)
    blog = db.Column(db.ForeignKey('Blog.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


