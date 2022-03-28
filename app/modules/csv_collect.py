import csv,io

# 共通的に使用できるcsv処理をまとめたメソッド
class CsvCollect():
	# CSV読込
	@staticmethod
	def read_csv(filepath,encoding):
		with open(filepath,encoding=encoding,newline='') as f:
			reader = csv.reader(f)
			data_list = [data for data in reader]
			return data_list

	# CSVデータの書込(ファイルオブジェクトへの書込)
	@staticmethod
	def write_csv(file_object,datalist):
		writer = csv.writer(file_object)
		writer.writerows(datalist)
		return True
	
	# StringIOを使用したCSVデータのみの作成(2次元配列から生成)
	@staticmethod
	def csv_string_io_create(datalist):
		f = io.StringIO()
		writer = csv.writer(f,quotechar='"',quoting=csv.QUOTE_ALL,lineterminator="\n")
		writer.writerows(datalist)
		return f.getvalue()
