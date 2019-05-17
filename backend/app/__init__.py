from flask import Flask
from flask_cors import CORS
from app.ext import init_ext
from app.settings import envs
from app.views import init_blue

def create_app():
	app = Flask(__name__,static_folder="./../../dist/static",template_folder="./../../dist")
	cors = CORS(app, resources={r"/getList": {"origins": "*"}})
	# 初始化配置
	app.config.from_object(envs.get('develop'))
	# 注册蓝图，初始化蓝图
	init_blue(app)
	# 初始化第三方插件和库
	init_ext(app)
	return app