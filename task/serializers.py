from rest_framework import serializers
from .models import Subscribers

class Subscriber_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Subscribers
		fields = ("__all__")