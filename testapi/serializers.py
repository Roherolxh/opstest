from rest_framework import serializers
from django.contrib.auth.models import User


class UserBaseSerializer(serializers.Serializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'is_staff')
	# fields = '__all__' 表示最终序列化返回的所有字段