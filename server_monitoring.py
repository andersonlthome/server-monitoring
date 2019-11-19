#This code is for monitoring the usage of CPU and Memory of your server/PC
#For use, you have to put the code to run when the OS starts
import psutil,pymongo,platform,time,datetime
#That exemple is connecting with MongoAtlas
db_connection = '' # ex: "mongodb+srv://user:password@cluster0-lm0fw.mongodb.net/db?retryWrites=true&w=majority"

print('Recording usage of CPU and Memory, second to second')
client = pymongo.MongoClient(db_connection)
db_engajei = client.engajei
server_data = db_engajei.server_data
while 1>0:
    try:
	    cpu_percent_usage = float(psutil.cpu_percent(1))
	    memory_usage = float(psutil.virtual_memory()._asdict().get('percent'))
	    name_server = platform.node()
	    date = datetime.datetime.now()
	    server_data.insert_one({'name_server':name_server,'memory_usage':memory_usage,'cpu_percent_usage':cpu_percent_usage,'date':date})
	    time.sleep(60)
	except:
		pass

