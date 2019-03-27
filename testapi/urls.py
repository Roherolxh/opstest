from rest_framework import routers
from django.urls import include
from django.conf.urls import url
from .views import UserBaseList
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
	# url(r'^usercreate/$', UserBaseCreate.as_view(), name='usercreate'),
	url(r'^userlist/$', UserBaseList.as_view(), name='userlist'),
	# url(r'^userdetail/(?P<pk>[0-9]+)/$', views.user_detail, name='user_detail'),
	# url(r'^userdetail/(?P<pk>[0-9]+)/$', UserBaseDetail.as_view(), name='user_detail'),
	url(r'^docs/$', schema_view, name='docs')  # 这里报错的话请查看前面的说明（红色字体说明）
]

