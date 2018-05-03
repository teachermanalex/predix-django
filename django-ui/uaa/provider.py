from allauth.socialaccount import app_settings
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class PredixUAA(ProviderAccount):
  def to_str(self):
    dflt = super(PredixUAA, self).to_str()
    return self.account.extra_data.get('user_name', dflt)


class PredixUAAProvider(OAuth2Provider):
  id = 'predix'
  name = 'Predix'
  account_class = PredixUAA

  def extract_uid(self, data):
    return data['user_id']

  def extract_common_fields(self, data):
    return dict(name=data.get('user_name'))

  def get_default_scope(self):
    scope = ['openid']
    return scope


provider_classes = [PredixUAAProvider]