import ast
from flask import jsonify,request,current_app
from blueprints import api
from .. import CsvCollect,DataEdit

# メンバー状態更新
@api.route("/mod_member", methods=["POST"])
def mod_member():
	if request.method == 'POST':
		data = request.data.decode()
		data_dict = ast.literal_eval(data)
		member_id = data_dict["memberId"]
		condition = data_dict["condition"]

		data_list = CsvCollect.read_csv(current_app.config['CSV_PATH'],current_app.config['ENC'])
		after_data_list = DataEdit.mod_csv(data_list,member_id,condition)

		mod_flg = False
		with open(current_app.config['CSV_PATH'], 'w',encoding=current_app.config['ENC'],newline='') as f:
			if CsvCollect.write_csv(f,after_data_list):
				mod_flg = True

		return jsonify({'result':'success'}) if mod_flg else jsonify({'result':'failure'})
