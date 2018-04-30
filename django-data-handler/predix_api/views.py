from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importing the Predix python SDK. See https://github.com/PredixDev/predixpy
import predix.admin.app
import predix.data.timeseries


import os
import requests
from pprint import pprint
import threading

# Use Serializers to read POST data
from . import serializers

class TimeSeriesView(APIView):

  def getAndIngest(self):
    """
    Queries the data simulator.
    Ingests each car's speed at that instance into Time Series.

    """

    # If VCAP_SERVICES exist, use that to load Time Series
    # If not, use the manifest file

    if 'VCAP_SERVICES' in os.environ:
      ts = predix.data.timeseries.TimeSeries()
    else:
      # Load the application from the manifest file.
      # If you don't specify a path, it defaults to the current directory.
      app = predix.admin.app.Manifest()
      ts = app.get_timeseries()

    # To run the ingestion on an interval, uncomment the line below.
    # threading.Timer(5.0, self.getAndIngest).start()
    try:
      r = requests.get(os.environ.get('SIMULATOR_API', 'http://10.15.25.83:8090/cars/simulator'))
      for data in r.json():
        pprint('Ingesting speed of {0} at {1}'.format(data['name'], data['currentTime']))
        ts.send(data['id']+'_speed', data['speed'], quality=3, timestamp=data['currentTime'])
      return 'success'
    except:
      return 'failure'

  def get(self, request):
    """Ingests the current data into Time Series when called"""

    status = self.getAndIngest()

    if(status == 'failure'):
      return Response({'status': 'failure'})
    elif(status == 'success'):
      return Response({'status': 'Ingested'})

class AssetView(APIView):

  def get(self, request):
    if 'VCAP_SERVICES' in os.environ:
      asset = predix.data.asset.Asset()
    else:
      app = predix.admin.app.Manifest()
      asset = app.get_asset()

    cars = asset.get_collection('/connected_car')
    for car in cars:
      car['latitude'] = asset.get_collection(car['location'])[0]['latitude']
      car['longitude'] = asset.get_collection(car['location'])[0]['longitude']

    return Response(cars)
