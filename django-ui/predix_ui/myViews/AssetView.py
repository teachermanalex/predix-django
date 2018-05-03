from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Decorators for APIs
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Predix Python SDK
import predix.admin.app
# Generic
import os
from pprint import pprint

@method_decorator(login_required(login_url='/accounts/predix/login/'), name='dispatch')
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