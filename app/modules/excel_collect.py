# 共通的に使用できるexcel処理をまとめたメソッド
class ExcelCollect():
	# ワークシートに1つの値の書き込み
	@staticmethod
	def write_excel_value(ws,value,row,col):
		ws.cell(row,col).value = value
		return ws

	# ワークシートに2次元配列の書き込み
	@staticmethod
	def write_excel_datalist(ws,datalist,start_row,start_col):
		for i,row in enumerate(datalist):
			for j,cell in enumerate(row):
				ws.cell(row=start_row + i, column=start_col + j, value=datalist[i][j])
		return ws
	