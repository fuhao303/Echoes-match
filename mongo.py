import pymongo
import os
import configparser
from datetime import datetime,timedelta
from Aviso import Warning


LOCAL_PATH = os.path.dirname(os.path.realpath(__file__))
config_ini = configparser.ConfigParser()
config_ini.read(os.path.join(LOCAL_PATH, 'config.py'))

TIME=int(config_ini['AVISO']['TIEMPO'])
DIR=str(config_ini['MONGO']['DIRECCION'])

class Mongodbs():
    def conectMongo():
	    myclient = pymongo.MongoClient(DIR)
	    mydb = myclient["Estaciones"]
	    mycol = mydb["sites"]
	    return mycol
	  
    def insertar(stationName, data,mycol):
	     datos={ 'station': stationName, 'date': datetime.fromtimestamp(data['t'][0]).utcnow().isoformat()}
	     print(datos)
	     mycol.insert_one(datos) 
	     mydoc = mycol.find().sort("date",-1)
	     return mydoc
	     
    def comprobacion(mydoc):
        if mydoc[1]:
            a=datetime.strptime(mydoc[0]['date'],'%Y-%m-%dT%H:%M:%S.%f')
            b=datetime.strptime(mydoc[1]['date'],'%Y-%m-%dT%H:%M:%S.%f')
            temp=a-b
            print(a)
            print(b)
            segundos = temp / timedelta(seconds=1)
            if abs(segundos) < TIME and segundos !=0  : #and mydoc[0]['station'] !=mydoc[1]['station']
                print('hay una diferencia de ')
                print (temp)
                Warning.slack()
            else:
                print('no hay error')


