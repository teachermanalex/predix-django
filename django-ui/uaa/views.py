import requests
from allauth.socialaccount.providers.oauth2.views import (
  OAuth2Adapter,
  OAuth2CallbackView,
  OAuth2LoginView,
)
from django.conf import settings
from .provider import PredixUAAProvider
from pprint import pprint

class PredixUAAAdapter(OAuth2Adapter):
  provider_id = PredixUAAProvider.id
  # access_token_url = 'https://ec147fcf-cb35-408a-af01-ce4a359388fd.predix-uaa.run.aws-usw02-pr.ice.predix.io/oauth/token'
  # authorize_url = 'https://ec147fcf-cb35-408a-af01-ce4a359388fd.predix-uaa.run.aws-usw02-pr.ice.predix.io/oauth/authorize'
  # profile_url = 'https://ec147fcf-cb35-408a-af01-ce4a359388fd.predix-uaa.run.aws-usw02-pr.ice.predix.io/userinfo'

  access_token_url = getattr(settings, 'UAA_URL', None)+'/oauth/token'
  authorize_url = getattr(settings, 'UAA_URL', None)+'/oauth/authorize'
  profile_url = getattr(settings, 'UAA_URL', None)+'/userinfo'

  def complete_login(self, request, app, token, **kwargs):
    headers = {
      "Authorization": "bearer " + token.token
    }
    extra_data = requests.get(self.profile_url, headers=headers)
    pprint('response {0}'.format(extra_data.json()))
    return self.get_provider().sociallogin_from_response(
      request,
      extra_data.json()
    )


oauth2_login = OAuth2LoginView.adapter_view(PredixUAAAdapter)
oauth2_callback = OAuth2CallbackView.adapter_view(PredixUAAAdapter)