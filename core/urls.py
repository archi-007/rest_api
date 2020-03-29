
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path('', views.TestView.as_view(), name = 'test'),
    path('api/token/', obtain_auth_token, name = 'obtain-token'),
]
