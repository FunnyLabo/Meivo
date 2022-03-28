from json import load
import os,importlib
import flask,blueprints
from logging.config import dictConfig
from flask import Flask

def create_app():
	with open("logging.json", "r", encoding="utf-8") as f:
		dictConfig(load(f))

	app = Flask(__name__, instance_relative_config=True)

	app.config.from_object("settings.AppConfig")
	if app.config["ENV"] == "development":
		app.config.from_pyfile(os.path.join("config", "development.py"), silent=True)
	else:
		app.config.from_pyfile(os.path.join("config", "production.py"), silent=True)

	for blueprint in blueprints.all_blueprints:
		importlib.import_module(blueprint.import_name)
		app.register_blueprint(blueprint)
	
	return app