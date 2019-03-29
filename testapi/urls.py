
from django.conf.urls import url
from .views import SwaggerSchemaView, ReturnJson, StudentsApiView

urlpatterns = [
	url(r'^api/$', ReturnJson.as_view(), name='api'),
	url(r'^api/v1/$', StudentsApiView.as_view(), name='api_v1'),
	url(r'^docs/', SwaggerSchemaView.as_view(), name='apiDocs'),
]

