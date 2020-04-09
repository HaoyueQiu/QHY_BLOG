from flask import Blueprint


bp = Blueprint('api',__name__) #注册蓝图(blueprint)

# 写在最后是为了防止循环导入bp
from app.api import test, auth, errors, token, users,blogs,upload
