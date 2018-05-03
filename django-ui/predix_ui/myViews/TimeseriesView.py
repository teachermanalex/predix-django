from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Decorators for APIs
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Predix Python SDK
import predix.admin.app
import predix.data.timeseries
# Generic
import os
from pprint import pprint
# User defined
from predix_ui import serializers

@method_decorator(login_required(login_url='/accounts/predix/login/'), name='dispatch')
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