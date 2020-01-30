import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__)) # 根目录
load_dotenv(os.path.join(basedir,'.env')) # 导入环境文件

class Config(object):
    pass
