from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from test_api.models import User
from test_api.serializers import UserSerializer

""" Api to list out all user.
Created serializers for user create and update user.
authenticating by token used jwt token.
endpoints are mensioned in readme file """

class UserViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticated]
	queryset = User.objects.all()
	serializer_class = UserSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filterset_fields = ('email', 'first_name')
