
def get_db_url(dbinfo):
	# DB = dbinfo.get('db')
	# HOST = dbinfo.get('host')
	# PORT = dbinfo.get('port')
	# USERNAME = dbinfo.get('username')
	# PASSWORD = dbinfo.get('password')
	return dbinfo

class DevelopConfig():
	# DEBUG = True
	DATABASE = {
		'db': 'test',
		'host': '192.168.4.108',
		'port': 27017,
		'username':'',
		'password':''
	}
	MONGO_DATABASE_URL = get_db_url(DATABASE)

envs = {
	'develop':DevelopConfig
}