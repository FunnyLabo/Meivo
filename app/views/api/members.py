from blueprints import api
from flask import current_app,jsonify
from .. import CsvCollect

# メンバー一覧
@api.route("/members", methods=["GET"])
def members():
	result_arr = []
	data_list = CsvCollect.read_csv(current_app.config['CSV_PATH'],current_app.config['ENC'])
	for row in data_list:
		obj = {}
		obj['id'] = row[0]
		obj['dev'] = row[1]
		obj['name'] = row[2]
		obj['condition'] = row[3]
		result_arr.append(obj)
	
	return jsonify({'result':result_arr})