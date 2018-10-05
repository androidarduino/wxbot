import pickle
class Config:
	auto_pull = True
	no_revoke = True
	remote_cmd = True
	group_send = True
	
	def load(self, file_name = 'default.cfg'):
		return pickle.load(open(file_name, 'rb'))	
	def dump(self, file_name = 'default.cfg'):
		pickle.dump(self, open(file_name, 'wb'))

config = Config.load()
