from django.shortcuts import render
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Subscribers


from .serializers import Subscriber_Serializer

class Add_Subscribers(APIView):
	def get_object(self, email):
		try:
			return Subscribers.objects.get(email=email)
		except Subscribers.DoesNotExist:
			return None

	def post(self,request,format=None):
		try:
			email = request.data.get('email')
			data_object = self.get_object(email)
			if data_object:
				serializer = serializer = Subscriber_Serializer(data_object,data=request.data)
			else:
				serializer = Subscriber_Serializer(data=request.data)
			if serializer.is_valid():
				serializer.save(active=True)
				return Response(serializer.data,status=status.HTTP_200_OK)
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
		except:
			return Response({"message":"An unknown error occurred"})
		


class Remove_Subscribers(APIView):

	def get_object(self, email):
		try:
			return Subscribers.objects.get(email=email)
		except Subscribers.DoesNotExist:
			return None

	def post(self,request,format=None):
		try:
			email = request.data.get('email')
			data_object = self.get_object(email)
			if data_object:
				serializer = Subscriber_Serializer(data_object,data=request.data,partial=True)
			else:
				return Response({"message":"Requested user does not exist"})	
			if serializer.is_valid():
				serializer.save(active=False)
				return Response({"message": "Removed from Subscribers list"})
		except:
			return Response({"message":"Requested user does not exist here"})

