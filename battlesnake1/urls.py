from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, views
from rest_framework.renderers import JSONRenderer

from . import views

urlpatterns = [
    # battlesnake API V2 - BattleSnake1
    path('api/v1/', views.hello, name="hello"),
    path('api/v1/start', views.start, name="start"),
    path('api/v1/move', views.move, name="move"),
    path('api/v1/end', views.end, name="end"),
]
