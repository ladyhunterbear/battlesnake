from django.contrib.auth.models import User, Group
from rest_framework import serializers

class CoordinateSerializer(serializers.Serializer):
    x = serializers.IntegerField(required=True)
    y = serializers.IntegerField(required=True)

class RulesetSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    version = serializers.CharField(required=True)

class GameSerializer(serializers.Serializer):
    id = serializers.CharField(required=True)
    ruleset = RulesetSerializer(required=True)
    timeout = serializers.IntegerField(required=True)

class SnakeSerializer(serializers.Serializer):
    id = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    health = serializers.IntegerField(required=True)
    body = CoordinateSerializer(required=True, many=True)
    latency = serializers.Serializer(required=True)
    head = CoordinateSerializer(required=True)
    length = serializers.IntegerField(required=True)
    shout = serializers.CharField(required=True)
    squad = serializers.CharField(required=True)

class BoardSerializer(serializers.Serializer):
    height = serializers.IntegerField(required=True)
    width = serializers.IntegerField(required=True)
    food = CoordinateSerializer(required=True, many=True)
    hazards = CoordinateSerializer(required=True, many=True)
    snakes = SnakeSerializer(required=True, many=True)

class MoveRequestSerializer(serializers.Serializer):
    game = GameSerializer(required=True)
    turn = serializers.IntegerField(required=True)
    board = BoardSerializer(required=True)
    you = SnakeSerializer(required=True)

