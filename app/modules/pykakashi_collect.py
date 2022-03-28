from pykakasi import kakasi

# 共通的に使用できるpykakasiの処理をまとめたメソッド
class PykakasiCollect():
	value = ""
	kakashi = ""
	def __init__(self,value):
		# 初期化処理
		self.kakasi = kakasi()
	
	# モードのセット(K:カタカナ、H:ひらがな、J:漢字、a:ローマ字、E:JISローマ字)
	def setConvertMode(self,from_value,to_value):
		self.kakashi = self.kakashi.setMode(from_value,to_value)
		
	# 入力値(文字列)を変換
	def strToConvert(self):
		conv = self.kakasi.getConverter()
		return conv.do(self.value)

	# 入力値(配列)を変換
	def arrToConvert(self):
		conv = self.kakasi.getConverter()
		return [conv.do(val) for val in self.value]

	