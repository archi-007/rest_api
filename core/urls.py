
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path('', views.PostView.as_view(), name = 'test'),
    path('list-create', views.PostListCreateView.as_view(), name = 'list-create'),
    path('create/', views.PostCreateView.as_view(), name = 'create'),
    path('api/token/', obtain_auth_token, name = 'obtain-token'),
    
]
