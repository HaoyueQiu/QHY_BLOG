# coding=utf-8
from app.api.errors import error_response
from app.models import User
from flask import g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


'''
Basic Auth是配合RESTful API使用的最简单的认证方式，客户端向服务器发请求时，会在请求的http header中提供用户名和密码作为认证信息
Flask虽然没有集成Basic Auth的实现，但相关信息均已提供，只需对basic auth装饰器进行简单封装即可实现Basic Auth，而后将该装饰器应用到需要使用basic auth的API中
https://www.jianshu.com/p/5e21506a9990
'''
@basic_auth.verify_password
def verify_password(username, password):
    """用于检查用户提供的用户名和密码"""
    user = User.query.filter_by(username=username).first()
    if user is None:
        return False
    g.current_user = user
    return user.check_password(password)


@basic_auth.error_handler
def basic_auth_error():
    """用于在认证失败的情况下返回错误响应"""
    return error_response(401)


@token_auth.verify_token
def verify_token(token):
    """用于检查用户请求是否有token，并且token真实存在，还在有效期内"""
    g.current_user = User.check_token(token) if token else None
    return g.current_user is not None


@token_auth.error_handler
def token_auth_error():
    """用于在 Token Auth 认证失败的情况下返回错误响应"""
    return error_response(401)
