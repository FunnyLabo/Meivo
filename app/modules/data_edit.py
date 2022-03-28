from .common import Common

# 共通的に使用できるデータ加工処理をまとめたメソッド
class DataEdit():
	# メンバーの状態変化
	@staticmethod
	def  mod_csv(data_list,member_id,condition):
		for row in data_list:
			if row[0] == member_id:
				row[3] = Common._REQ_POST_CONDITION[condition]
		return data_list
	
	# 参加者を返す
	@staticmethod
	def return_join_member(datalist):
		datalist = list(filter(lambda row:row[3] == Common._REQ_POST_CONDITION[1],datalist))
		result_list = [[i,row[1],row[2]]for i,row in enumerate(datalist,1)]
		return result_list

	# 不参加者を返す
	@staticmethod
	def return_not_join_member(datalist):
		datalist = list(filter(lambda row:row[3] == Common._REQ_POST_CONDITION[0] or row[3] == Common._REQ_POST_CONDITION[2],datalist))
		result_list = [[i,row[1],row[2]]for i,row in enumerate(datalist,1)]
		return result_list
