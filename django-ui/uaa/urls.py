from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import PredixUAAProvider


urlpatterns = default_urlpatterns(PredixUAAProvider)