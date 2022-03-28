from blueprints import top_page
from flask import render_template

# 起点ページレンダリング
@top_page.route('/')
def index():
	return render_template('index.html')
