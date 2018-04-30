from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^timeseries/ingest', views.TimeSeriesView.as_view()),
  url(r'^asset/cars', views.AssetView.as_view()),
]