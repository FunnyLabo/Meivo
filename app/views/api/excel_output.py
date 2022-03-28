from blueprints import api
import os,openpyxl,datetime
from flask import current_app,make_response
from .. import CsvCollect,DataEdit,ResponseCreate,ExcelCollect

# Excelダウンロード
@api.route("/excel_output", methods=["GET"])
def excel_output():
	d_now = datetime.date.today()
	fmt_d_now = d_now.strftime('%Y/%m/%d')
	datalist = CsvCollect.read_csv(current_app.config['CSV_PATH'],current_app.config['ENC'])
	response = make_response()
	wb = openpyxl.load_workbook(current_app.config['EXCEL_TEMPLATE_PATH'])
	ws = wb[current_app.config['EXCEL_TEMPLATE_SHEET_NAME']]
	# タイトルの書き込み
	ws = ExcelCollect.write_excel_value(ws,"忘年会テスト",1,2)
	# 作成日時の書き込み
	ws = ExcelCollect.write_excel_value(ws,"作成日時："+ fmt_d_now,2,6)
	# 参加者の読込+書き込み
	join_list = DataEdit.return_join_member(datalist)
	ws = ExcelCollect.write_excel_datalist(ws,join_list,5,2)
	# 不参加者の読込+書き込み
	not_join_list = DataEdit.return_not_join_member(datalist)
	ws = ExcelCollect.write_excel_datalist(ws,not_join_list,5,5)
	wb.save(current_app.config['EXCEL_WORK_PATH'])
	wb.close()
	wb = open(current_app.config['EXCEL_WORK_PATH'], "rb" )
	response_data = wb.read()
	wb.close()
	response = ResponseCreate.excel_response_create(response,response_data,current_app.config['EXCEL_OUTPUT_FILENAME'])
	# 一時Excelファイルの削除
	os.remove(current_app.config['EXCEL_WORK_PATH'])
	return response