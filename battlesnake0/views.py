from django.shortcuts import render #needed?
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from battlesnake0.serializers import MoveRequestSerializer
from rest_framework.renderers import JSONRenderer
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from battlesnake0.gamemove import GameMove
from battlesnake0.gameboard import GameBoard

def index(request):
    if request.method == 'GET':
        return JsonResponse({"message":"GET IT!"})
    elif request.method == 'POST':
        return HttpResponse("POST IT!")

@csrf_exempt
def start(request):
    if request.method == 'GET':
        return JsonResponse({"message": "Start GET"})
    elif request.method == 'POST':
        return JsonResponse({"message": "Start POST"})

@csrf_exempt
@require_http_methods(["POST"])
def move(request):
    res = {}
    try:
        req = json.loads(request.body.decode("utf-8"))
        #req = request.body.decode("utf-8")
    except Exception as e:
        res["details"] = "Invalid request body"
        return JsonResponse(res, status.HTTP_400_BAD_REQUEST)
    
    
    gameboard = GameBoard( req['board']['height'], req['board']['width'] )
    gameboard.add_food( req['board']['food'] )
    gameboard.add_hazards( req['board']['hazards'] )
    gameboard.add_my_snake( req['you'] )
    gameboard.add_snakes( req['board']['snakes'] )
    game_move = GameMove(gameboard)
    response = game_move.get_move()
    return JsonResponse(response)

@csrf_exempt
@require_http_methods(["POST"])
def end(request):
    res = {}
    if request.method == 'GET':
        return JsonResponse({"message": "End GET"})
    elif request.method == 'POST':
        try:
            req = json.loads(request.body.decode("utf-8"))
        except Exception as e:
            res["details"] = "Invalid request body"
            return JsonResponse(res, status.HTTP_400_BAD_REQUEST)

        serializer = MoveRequestSerializer(req)
        
        return JsonResponse(serializer.data)
