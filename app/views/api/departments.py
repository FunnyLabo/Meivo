import ast
from flask import jsonify,request,current_app
from blueprints import api
from .. import CsvCollect,DataEdit

# CSV内の部署一覧を返す
@api.route("/departments", methods=["GET"])
def departments():
	data_list = CsvCollect.read_csv(current_app.config['CSV_PATH'],current_app.config['ENC'])
	unique_deptlist = list(set(row[1] for row in data_list))
	unique_deptlist.insert(0,"")
	return jsonify({'result':unique_deptlist})
