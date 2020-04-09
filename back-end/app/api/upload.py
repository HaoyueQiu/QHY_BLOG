# -*- coding: UTF-8 -*-
from flask import jsonify
from flask import request

from app.api import bp
from app.api.auth import token_auth


# from app.models import Post


@bp.route('/upload', methods=['POST'])
@token_auth.login_required
def upload_pic():
    '''添加一张新图片'''
    return