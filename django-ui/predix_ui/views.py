from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importing the Predix python SDK. See https://github.com/PredixDev/predixpy
import predix.admin.app
import predix.data.timeseries

from . import serializers

import os
import requests
from pprint import pprint

class TimeseriesView(APIView):
  def post(self, request):
    # If VCAP_SERVICES exist, use that to load Time Series
    # If not, use the manifest file
    if 'VCAP_SERVICES' in os.environ:
      ts = predix.data.timeseries.TimeSeries()
    else:
      # Load the application from the manifest file.
      # If you don't specify a path, it defaults to the current directory.
      app = predix.admin.app.Manifest()
      ts = app.get_timeseries()

    serializer = serializers.ReqSerializer(data=request.data)

    if(serializer.is_valid()):
      pprint('Getting latest datapoint of {0}'.format(serializer.data.get('tag')))
      try:
        return Response(ts.get_latest('CC1_speed'))
      except Exception as e:
        pprint(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssetView(APIView):
  def get(self, requests):
    if 'VCAP_SERVICES' in os.environ:
      asset = predix.data.asset.Asset()
    else:
      app = predix.admin.app.Manifest()
      asset = app.get_asset()

    try:
      cars = asset.get_collection('/connected_car')
      for car in cars:
        car['latitude'] = asset.get_collection(car['location'])[0]['latitude']
        car['longitude'] = asset.get_collection(car['location'])[0]['longitude']
      return Response(cars)
    except:
      return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def dashboard(request):
  data = {}
  # os.environ.get('ASSET_API', )
  # template = loader.get_template("predix_ui/dashboard.html")
  return render(request, 'predix_ui/dashboard.html', data)