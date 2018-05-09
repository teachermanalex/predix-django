# Importing the Predix python SDK. See https://github.com/PredixDev/predixpy
import predix.admin.app
import predix.data.timeseries

import os
import requests
from pprint import pprint
import threading
import datetime

def getAndIngest(ts):
  pprint('***************************')
  try:
    simulator = os.environ.get('SIMULATOR_API')
    r = requests.get(simulator+'/cars/simulator')
    for data in r.json():
      timestamp = datetime.datetime.fromtimestamp(int(data['currentTime'])/1000).strftime('%c')
      pprint('Ingesting speed of {0} at UTC: {1}'.format(data['name'], timestamp))
      ts.send(data['id']+'_speed', data['speed'], quality=3, timestamp=data['currentTime'])
  except:
    pprint('Ingest Failed')
  pprint('***************************')

  # To run the ingestion on an interval, uncomment the line below.
  threading.Timer(5.0, getAndIngest, [ts]).start()

def ready():
  if 'VCAP_SERVICES' in os.environ:
    ts = predix.data.timeseries.TimeSeries()
    getAndIngest(ts)
  else:
    # Load the application from the manifest file.
    # If you don't specify a path, it defaults to the current directory.
    app = predix.admin.app.Manifest()
    ts = app.get_timeseries()
    getAndIngest(ts)