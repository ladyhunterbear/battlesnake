from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, views
from rest_framework.renderers import JSONRenderer

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api-auth/', include('rest_framework.urls')),
    # battlesnake API
    path('api/v1/start/', views.start, name="start"),
    path('api/v1/move/', views.move, name="move"),
    path('api/v1/end/', views.end, name="end"),
]