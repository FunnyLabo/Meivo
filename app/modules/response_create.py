from .common import Common

# 共通的に使用できるFlaskレスポンスオブジェクト作成処理をまとめたメソッド
class ResponseCreate():
	# Excel用Flaskレスポンスオブジェクト作成
	@staticmethod
	def  excel_response_create(response,data,output_filename):
		response.data = data
		#ダウンロードするEXCELファイル名を設定
		response.headers[ "Content-Disposition" ] = "attachment; filename=" + output_filename
		response.mimetype = Common.XLSX_MIMETYPE

		return response

	# CSV用Flaskレスポンスオブジェクト作成
	@staticmethod
	def  csv_response_create(response,data,output_filename):
		response.data = data
		#ダウンロードするCSVファイル名を設定
		response.headers['Content-Type'] = 'text/csv'
		response.headers['Content-Disposition'] = 'attachment;filename=' + output_filename
		return response
	