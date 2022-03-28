from blueprints import api
from flask import current_app,make_response
from .. import CsvCollect,ResponseCreate

# CSVダウンロード(フロント側：res.dataで中身取得可能)
@api.route("/csv_output", methods=["GET"])
def csv_output():
	response = make_response()
	datalist = CsvCollect.read_csv(current_app.config['CSV_PATH'],current_app.config['ENC'])
	csvdata = CsvCollect.csv_string_io_create(datalist)
	response = ResponseCreate.csv_response_create(response,csvdata,current_app.config['CSV_OUTPUT_FILENAME'])
	return response
