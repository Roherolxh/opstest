#from django.contrib import admin
from django.urls import include
from django.conf.urls import url
from simple_sso.sso_client.client import Client
from django.conf import settings
from . import views

test_client = Client(settings.SSO_SERVER, settings.SSO_PUBLIC_KEY, settings.SSO_PRIVATE_KEY)

urlpatterns = [
    url(r'^client/', include(test_client.get_urls())),
	url(r'test/', views.testClientSSO, name='testSSO'),
]