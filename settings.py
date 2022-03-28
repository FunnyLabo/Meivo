# 標準設定 (公開) ファイル
# 非公開設定ファイルは instance ディレクトリへ配置する
class AppConfig(object):
	ENV = 'development'
	DEBUG = True
	TESTING = False
	# オブジェクトをASCIIでエンコードされたJSONにシリアライズ
	# Falseにするとjsonifyから返すJSONはunicodeを含むようになる
	JSON_AS_ASCII = False
	CSV_PATH = "./static/csv/index.csv"
	ENC = "utf-8"
	EXCEL_TEMPLATE_PATH = "./static/excel/template/template.xlsx"
	EXCEL_TEMPLATE_SHEET_NAME = "名簿シート"
	EXCEL_WORK_PATH = "./static/excel/work.xlsx"
	EXCEL_OUTPUT_FILENAME = "output.xlsx"
	CSV_OUTPUT_FILENAME = "output.csv"
