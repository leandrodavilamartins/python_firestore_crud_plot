#complete crud from firestore and plotting with matplotlib / seaborn . 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates
from datetime import datetime
import seaborn as sns

sns.set_theme()

cred = credentials.Certificate('esp32-firebase-1c18f-firebase-adminsdk-ytlcj-47aaa3ad59.json') # private key file reference
firebase_admin.initialize_app(cred)
db = firestore.client()

docs = db.collection('sensorData').get()

humidity = []
temperature = []
timestamp = []
formattedData = []

for doc in docs:
    humidity.append(doc.to_dict()['humidity'])
    temperature.append(doc.to_dict()['temperature'])
    ts = int(doc.to_dict()['timestamp']) / 1000 # time must be in seconds ! 
    tempo = datetime.fromtimestamp(ts) 
    #print(tempo)
    formattedData.append(tempo)


#print(humidity)
#print('')
#print(temperature)
print(datetime)
dates = matplotlib.dates.date2num(formattedData)
print(dates)
plt.plot_date(dates,humidity)
plt.show()