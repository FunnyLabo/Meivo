# モジュール内共通変数等の定義
class Common():
	#  CSVに合わせキーは「0:不参加,1:参加,2:未定」で表す
	_REQ_POST_CONDITION = {
		0:'不参加',
		1:'参加',
		2:'未定'
	}

	# Excelレスポンス用MINEタイプ
	XLSX_MIMETYPE = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
