from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^latest$', views.TimeseriesView.as_view()),
  url(r'^assets$', views.AssetView.as_view()),
  url(r'^.*$', views.dashboard, name='index'),
]