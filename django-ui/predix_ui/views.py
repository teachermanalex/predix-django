from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.decorators import login_required

# Importing the Predix python SDK. See https://github.com/PredixDev/predixpy
import predix.admin.app
import predix.data.timeseries

import os
import requests
from pprint import pprint

@login_required(login_url='/accounts/predix/login/')
def dashboard(request):
  data = {}
  # os.environ.get('ASSET_API', )
  # template = loader.get_template("predix_ui/dashboard.html")
  return render(request, 'predix_ui/dashboard.html', data)