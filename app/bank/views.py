from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer














# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Customer

# # def read(request):
# #     user_name = request.GET.get('username')
# #     query_read = Customer.objects.filter(
# #         customer_name = user_name
# #     )
# #     return HttpResponse (query_read.values())

# # Create your views here.
