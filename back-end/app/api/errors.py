# coding=utf-8
from app import db
from app.api import bp
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


@bp.app_errorhandler(400)
def bad_request(message):
    # 最常用的错误 400：错误的请求
    return error_response(400, message)


'''
在默认的http请求中，如果没有进行特别的自定义需求，那么出现404错误之类的，则会显示Not Found等信息。
如果需要在发生错误的时候，再进行一系列的业务处理，这时候就可以使用自定义的错误处理方法。

而在Flask view函数中，如果需要中断request，可以使用abort(500)或者直接抛异常raise exception。
中断request后需要返回一个出错信息给前端，所以就对errorhandler进行定制。
一般只需要两个handler即可，一个是404错误，一个是500一类的服务器端错误。
app_errorhandler 会自动捕捉全局状态码，如此便可以进行错误定制

'''
@bp.app_errorhandler(404)
def not_found_error(error):
    return error_response(404)


@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return error_response(500)

