from flask import Flask
from config import Config
from flask_cors import CORS

def create_app(config_class=Config):

    app = Flask(__name__) #创建flask应用
    app.config.from_object(config_class) #导入config设置

    CORS(app)
    
    from app.api import bp as api_bp
    app.register_blueprint(api_bp,url_prefix='/api') #注册蓝图，要使用该蓝图即加前缀/api

    return app

