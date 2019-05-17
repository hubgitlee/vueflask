from flask import Blueprint,render_template
from flask import request
from flask_restful import Api,Resource
from app.models import GlobalFiler
from bson import json_util
import json,time,datetime
blue = Blueprint('first_blue',__name__)

# def init_restful(blue):
	
api = Api(blue)
def init_blue(app):
	app.register_blueprint(blueprint=blue)
	

class Hello(Resource):
   def get(self):
        return 'hello world!'


api.add_resource(Hello, '/hello', endpoint="hello")


@blue.route('/',defaults={'path':''})
@blue.route('/<path:path>')
def catch_all(path):
	return render_template("index.html")
# @blue.route('/')
# def index():
# 	return 'hello world!'

@blue.route('/add/',methods=['POST'])
def add():
	print(request.get_json(force=True))
	# data = json.loads(request.get_data())
	# # username = request.form.getlist('username')
	# print(data)
	
	# c = request.data() 
	p = GlobalFiler()
	p.SampleID='1'
	p.D3S1358='2'
	p.vWA='3'
	p.D16S539='4'
	p.CSF1PO='5'
	p.TPOX='6'
	p.Yindel='7'
	p.Amel='8'
	p.D8S1179='9'
	p.D21S11='10'
	p.D18S51='11'
	p.DYS391='12'
	p.D2S441='13'
	p.D19S433='14'
	p.TH01='15'
	p.FGA='16'
	p.D22S1045='17'
	p.D5S818='18'
	p.D13S317='19'
	p.D7S820='20'
	p.SE33='21'
	p.D10S1248='22'
	p.D1S1656='23'
	p.D12S391='24'
	p.D2S1338='25'
	p.save()
	result={"status":"SUCCESS","message":"执行成功"}
	return json.dumps(result)

@blue.route('/getpersons/')
def get_persons():
	# persons = Person.objects
	for globalfiler in GlobalFiler.objects:
		print(globalfiler.SampleID)
	# print(type(persons))
	return 'okok'
	# return render_template('PersonList.html',persons=persons)

# @blue.route('/queryList/',methods=['GET','POST'])
# def getList():
# 	datalist = []
# 	t2 = []
# 	t1 = ['_id','SampleID','D3S1358','vWA','D16S539','CSF1PO','TPOX','Yindel','Amel','D8S1179','D21S11','D18S51','DYS391','D2S441','D19S433','TH01','FGA','D22S1045','D5S818','D13S317','D7S820','SE33','D10S1248','D1S1656','D12S391','D2S1338','add_time']
# 	# persons = GlobalFiler.objects
# 	for globalfiler in GlobalFiler.objects:
# 		for i in range(len(t1)):
# 			if t1[i] in ['add_time']:
# 				t2.append(eval('globalfiler.'+t1[i]).strftime('%Y-%m-%d %H:%M:%S'))
# 			elif t1[i] in ['_id']:
# 				tm = json_util.dumps(globalfiler.id)
# 				t2.append(tm)
# 			else:
# 				t2.append(eval('globalfiler.'+t1[i]))
# 		dic = dict(zip(t1,t2))
# 		datalist.append(dic)
# 		t2 = []
		
# 	dictm = {"status":"SUCCESS","message":"执行成功","data":datalist,"count":2}
# 	return json.dumps(dictm)

class getList(Resource):
	def getList(self):
		datalist = []
		t2 = []
		t1 = ['_id','SampleID','D3S1358','vWA','D16S539','CSF1PO','TPOX','Yindel','Amel','D8S1179','D21S11','D18S51','DYS391','D2S441','D19S433','TH01','FGA','D22S1045','D5S818','D13S317','D7S820','SE33','D10S1248','D1S1656','D12S391','D2S1338','add_time']
		# persons = GlobalFiler.objects
		for globalfiler in GlobalFiler.objects:
			for i in range(len(t1)):
				if t1[i] in ['add_time']:
					t2.append(eval('globalfiler.'+t1[i]).strftime('%Y-%m-%d %H:%M:%S'))
				elif t1[i] in ['_id']:
					tm = json_util.dumps(globalfiler.id)
					t2.append(tm)
				else:
					t2.append(eval('globalfiler.'+t1[i]))
			dic = dict(zip(t1,t2))
			datalist.append(dic)
			t2 = []
			
		dictm = {"status":"SUCCESS","message":"执行成功","data":datalist,"count":2}
		return json.dumps(dictm)
api.add_resource(getList, '/queryList', endpoint="queryList")

@blue.route('/delete/',methods=['GET','POST'])
def delete():
	print('oooo')
	return 'chengong'



	# ss = '''
	# 	{
	# 		"status": "SUCCESS",
	# 		"message": "执行成功",
	# 		"data": [{
	# 			"id": "41fB278a-d93D-EAfc-47d9-9278ff6997e8",
	# 			"title": "周杰标题",
	# 			"content": "邓伟内容内容内容内容内容内容",
	# 			"publicState": "未发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "2002-12-28 20:07:57",
	# 			"updateTime": "1983-07-18 01:24:56",
	# 			"creator": "钱娜",
	# 			"viewCount": 15
	# 		}, {
	# 			"id": "DDc5a7A4-ce1e-C5B3-f6fE-ff9eD972AFB7",
	# 			"title": "罗秀兰标题",
	# 			"content": "锺秀兰内容内容内容内容内容内容",
	# 			"publicState": "已发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "2010-10-19 04:36:46",
	# 			"updateTime": "2000-04-15 07:08:06",
	# 			"creator": "邵霞",
	# 			"viewCount": 69
	# 		}, {
	# 			"id": "7Cc2eE60-cAC5-4328-CDdf-1d0cfbC6e7B7",
	# 			"title": "朱桂英标题",
	# 			"content": "吕桂英内容内容内容内容内容内容",
	# 			"publicState": "未发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "1981-04-25 17:02:44",
	# 			"updateTime": "1980-12-31 18:53:13",
	# 			"creator": "唐明",
	# 			"viewCount": 38
	# 		}, {
	# 			"id": "52daE81d-Cf2D-eB95-03f5-8c635b2F3AC8",
	# 			"title": "张勇标题",
	# 			"content": "钱秀兰内容内容内容内容内容内容",
	# 			"publicState": "已发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "2012-09-27 17:44:26",
	# 			"updateTime": "2000-05-01 17:03:29",
	# 			"creator": "薛静",
	# 			"viewCount": 48
	# 		}, {
	# 			"id": "B9b97baA-A3db-66B5-3D87-bbF09EB2dAfa",
	# 			"title": "彭杰标题",
	# 			"content": "侯刚内容内容内容内容内容内容",
	# 			"publicState": "已发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "2016-05-09 11:58:57",
	# 			"updateTime": "1986-01-11 07:55:15",
	# 			"creator": "锺娜",
	# 			"viewCount": 148
	# 		}, {
	# 			"id": "41eEf5bD-1f73-6FCd-2CE2-3EeF5Cf37Bb6",
	# 			"title": "孙娜标题",
	# 			"content": "程强内容内容内容内容内容内容",
	# 			"publicState": "已发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "2008-10-12 06:54:41",
	# 			"updateTime": "2014-01-20 19:59:09",
	# 			"creator": "孙娜",
	# 			"viewCount": 21
	# 		}, {
	# 			"id": "EEbbe7Ef-bdb8-Ba10-b396-ADbAC722c6A9",
	# 			"title": "方娟标题",
	# 			"content": "吴丽内容内容内容内容内容内容",
	# 			"publicState": "已发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "1970-05-11 19:25:27",
	# 			"updateTime": "2004-06-15 12:41:28",
	# 			"creator": "方磊",
	# 			"viewCount": 94
	# 		}, {
	# 			"id": "6e1F97c3-1D5D-37b5-06FC-cCcF58dabABb",
	# 			"title": "邵涛标题",
	# 			"content": "江芳内容内容内容内容内容内容",
	# 			"publicState": "已发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "1976-03-15 08:20:32",
	# 			"updateTime": "1985-09-09 01:05:24",
	# 			"creator": "蔡涛",
	# 			"viewCount": 109
	# 		}, {
	# 			"id": "9ED0efe0-78f1-f64b-4a78-33Bd125D9ff2",
	# 			"title": "罗丽标题",
	# 			"content": "冯霞内容内容内容内容内容内容",
	# 			"publicState": "已发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "1978-07-08 06:29:09",
	# 			"updateTime": "1974-04-26 14:26:38",
	# 			"creator": "陆涛",
	# 			"viewCount": 22
	# 		}, {
	# 			"id": "60DEC2DC-2168-85dc-dcB4-E4D0C6FfaA56",
	# 			"title": "白洋标题",
	# 			"content": "范芳内容内容内容内容内容内容",
	# 			"publicState": "未发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "1976-06-22 14:17:12",
	# 			"updateTime": "2008-01-07 05:43:20",
	# 			"creator": "赖明",
	# 			"viewCount": 135
	# 		}, {
	# 			"id": "e62cDddc-Abff-fd56-EEcA-74aF3EfA5d63",
	# 			"title": "叶明标题",
	# 			"content": "范芳内容内容内容内容内容内容",
	# 			"publicState": "已发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "1991-06-02 23:09:09",
	# 			"updateTime": "2007-07-14 12:35:39",
	# 			"creator": "文娟",
	# 			"viewCount": 158
	# 		}, {
	# 			"id": "310d3a7e-ec43-77e5-dF59-CEcE7FbFD15e",
	# 			"title": "许强标题",
	# 			"content": "武敏内容内容内容内容内容内容",
	# 			"publicState": "已发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "2018-11-21 07:00:03",
	# 			"updateTime": "2012-06-04 07:46:09",
	# 			"creator": "龙勇",
	# 			"viewCount": 131
	# 		}, {
	# 			"id": "CE27fCac-FdC1-554c-8662-F9cc6E408Db4",
	# 			"title": "高秀英标题",
	# 			"content": "武丽内容内容内容内容内容内容",
	# 			"publicState": "未发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "2017-04-02 07:15:42",
	# 			"updateTime": "1988-09-06 04:52:55",
	# 			"creator": "陆娜",
	# 			"viewCount": 84
	# 		}, {
	# 			"id": "53D140C1-9f76-C75B-7473-B7AF4D27d8Eb",
	# 			"title": "叶秀兰标题",
	# 			"content": "董军内容内容内容内容内容内容",
	# 			"publicState": "已发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "1983-08-07 20:56:03",
	# 			"updateTime": "1987-10-31 01:45:05",
	# 			"creator": "曾军",
	# 			"viewCount": 178
	# 		}, {
	# 			"id": "a63fef5d-52A6-F389-4005-dfD1A3E7FE44",
	# 			"title": "叶霞标题",
	# 			"content": "锺明内容内容内容内容内容内容",
	# 			"publicState": "未发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "1970-02-07 10:33:53",
	# 			"updateTime": "2001-10-23 21:28:31",
	# 			"creator": "熊强",
	# 			"viewCount": 193
	# 		}, {
	# 			"id": "9247e255-88a5-d784-493E-7dC595fd21C2",
	# 			"title": "金霞标题",
	# 			"content": "马静内容内容内容内容内容内容",
	# 			"publicState": "未发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "1996-02-17 01:47:12",
	# 			"updateTime": "1997-02-16 12:16:39",
	# 			"creator": "蔡军",
	# 			"viewCount": 195
	# 		}, {
	# 			"id": "edC69c9E-FD0f-Db9c-c22A-dC8ABba1FBDB",
	# 			"title": "高刚标题",
	# 			"content": "孔强内容内容内容内容内容内容",
	# 			"publicState": "未发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "1975-09-09 22:08:44",
	# 			"updateTime": "1974-07-11 18:40:04",
	# 			"creator": "毛军",
	# 			"viewCount": 105
	# 		}, {
	# 			"id": "2a4451cd-361F-EceB-beB7-bcd69e5d8E07",
	# 			"title": "龚军标题",
	# 			"content": "康芳内容内容内容内容内容内容",
	# 			"publicState": "已发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "1991-06-16 20:21:53",
	# 			"updateTime": "2006-01-30 17:19:50",
	# 			"creator": "赖勇",
	# 			"viewCount": 108
	# 		}, {
	# 			"id": "469f5f4e-05b3-398f-F1BD-c78be5fD847c",
	# 			"title": "秦洋标题",
	# 			"content": "胡勇内容内容内容内容内容内容",
	# 			"publicState": "未发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "1972-06-05 23:34:31",
	# 			"updateTime": "1979-02-04 16:44:13",
	# 			"creator": "钱洋",
	# 			"viewCount": 53
	# 		}, {
	# 			"id": "b7e46ECA-b05E-86bc-FCC2-C25698Fd5eB5",
	# 			"title": "乔强标题",
	# 			"content": "孙敏内容内容内容内容内容内容",
	# 			"publicState": "已发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "1995-06-30 03:15:23",
	# 			"updateTime": "1986-02-07 18:41:47",
	# 			"creator": "薛刚",
	# 			"viewCount": 111
	# 		}, {
	# 			"id": "E6B8ACeB-B3cB-CbEc-D9D1-3DFcC6DbDe53",
	# 			"title": "尹洋标题",
	# 			"content": "汪磊内容内容内容内容内容内容",
	# 			"publicState": "未发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "1973-02-13 23:11:19",
	# 			"updateTime": "1976-05-12 18:28:24",
	# 			"creator": "方强",
	# 			"viewCount": 34
	# 		}, {
	# 			"id": "9233aE51-0De6-35cF-fbf1-37AEebd1Ba2E",
	# 			"title": "李磊标题",
	# 			"content": "谢超内容内容内容内容内容内容",
	# 			"publicState": "未发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "1985-04-05 22:21:40",
	# 			"updateTime": "1991-06-13 03:27:20",
	# 			"creator": "邓磊",
	# 			"viewCount": 63
	# 		}, {
	# 			"id": "571bbbeE-D97B-1Fd8-B491-E4AF6A7594A3",
	# 			"title": "朱秀兰标题",
	# 			"content": "崔秀兰内容内容内容内容内容内容",
	# 			"publicState": "已发布",
	# 			"keywords": ["关键字1", "关键字2"],
	# 			"depositoryBank": "存管银行",
	# 			"businessType": "业务类型",
	# 			"businessScene": "业务场景",
	# 			"createTime": "1989-07-31 13:31:36",
	# 			"updateTime": "2006-11-01 15:05:47",
	# 			"creator": "冯涛",
	# 			"viewCount": 192
	# 		}],
	# 		"count": 23
	# 	}
	# '''
	# print(type(ss))
	# print(type(json.loads(ss)))
	# return ss