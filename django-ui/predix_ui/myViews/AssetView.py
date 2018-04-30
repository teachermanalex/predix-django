from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import predix.admin.app

import os
from pprint import pprint

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