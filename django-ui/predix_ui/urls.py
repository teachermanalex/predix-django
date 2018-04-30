from django.conf.urls import url
from . import views
from predix_ui.myViews import TimeseriesView
from predix_ui.myViews import AssetView

urlpatterns = [
  url(r'^latest$', TimeseriesView.TimeseriesView.as_view()),
  url(r'^assets$', AssetView.AssetView.as_view()),
  url(r'^.*$', views.dashboard, name='index'),
]