# -*- coding: UTF-8 -*-
from flask import jsonify
from flask import request
import requests
import urllib
from app.api import bp
from app.api.auth import token_auth


# from app.models import Post


@bp.route('/blogs', methods=['POST'])
@token_auth.login_required
def create_post():
    '''添加一篇新文章'''
    pass


@bp.route('/blogs', methods=['GET'])
def get_blog():
    '''返回一篇文章'''
    '''通过id 返回文章？'''
    data = request.get_json()
    '''
        通过传入的参数决定要返回什么文章
    '''
    # post = Post.query.get_or_404(id)
    # post.views += 1
    # db.session.add(post)
    # db.session.commit()
    url = 'http://127.0.0.1:8800/CVPR 2018 DGNN/Skeleton-Based Action Recognition with Directed Graph Neural Network.md'

    f = urllib.request.urlopen(url)
    content = f.read().decode('utf-8')
    post = {'title': 'plan', 'content':content}
    return jsonify(post)


@bp.route('/blogs/<int:id>', methods=['PUT'])
# @token_auth.login_required
def update_post(id):
    '''修改一篇文章'''
    pass


@bp.route('/blogs/<int:id>', methods=['DELETE'])
# @token_auth.login_required
def delete_post(id):
    '''删除一篇文章'''
    pass

