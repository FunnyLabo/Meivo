from flask import Blueprint

top_page = Blueprint('top_page',import_name='app.views.top_page',url_prefix='/',template_folder='templates')
api = Blueprint('api',import_name='app.views.api',url_prefix='/api')

all_blueprints = (
	top_page,
	api,
)