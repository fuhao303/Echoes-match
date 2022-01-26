import requests
import os
import time
import configparser
from datetime import datetime

class  Warning():
    def slack():  
    #leer el url del bot
      LOCAL_PATH=os.path.dirname(os.path.realpath(__file__))
      config_ini=configparser.ConfigParser()
      config_ini.read(os.path.join(LOCAL_PATH,'config.py'))
      datos=str(config_ini['SLACK']['URL'])
      url =datos  
      msg='Ha habido un error a las '+str(datetime.now())
      r = requests.post(url, json={'text':msg})
      if(r.text == 'ok'):
        print('El aviso ha sido enviado')
        
      else:
        print(r.text)
     
    
