from django.shortcuts import render #needed?
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from battlesnake2.serializers import MoveRequestSerializer
from rest_framework.renderers import JSONRenderer
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from battlesnake2.game import Game


def index(request):
    if request.method == 'GET':
        return JsonResponse({"message":"GET IT!"})
    elif request.method == 'POST':
        return HttpResponse("POST IT!")

@csrf_exempt
@require_http_methods(["POST"])
def start(request):
    return JsonResponse({"message": "Sssssstart!"})


@csrf_exempt
@require_http_methods(["GET"])
def hello(request):
    return JsonResponse({
        "apiversion": "1",
        "author": "jharper",
        "color": "#D83727",
        "head": "orca",
        "tail": "rocket",
    })

@csrf_exempt
@require_http_methods(["POST"])
def move(request):
    res = {}
    try:
        req = json.loads(request.body.decode("utf-8"))
    except Exception as e:
        res["details"] = "Invalid request body"
        return JsonResponse(res, status.HTTP_400_BAD_REQUEST)
    response = Game(req).get_move()
    return JsonResponse(response)

@csrf_exempt
@require_http_methods(["POST"])
def end(request):
    return JsonResponse({"message": "Fin."})

