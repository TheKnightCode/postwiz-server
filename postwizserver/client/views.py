from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def status(request):
    if request.method != "GET": #Esta URL so aceita GET
        return HttpResponse(None, status = 405)

    with open("./database/mailHistory.json") as jsonFile:
        jsonData = json.load(jsonFile)

    try:
        return JsonResponse(jsonData[0]) #Retorna o estado atual da caixa representado como o primeiro objeto de jsonData
    except IndexError: #Caso ainda nao tenha nenhum dado no historico, envia "null" e responde com codigo HTTP 204
        return JsonResponse(data = None, safe = False, status = 204)

def history(request):
    if request.method != "GET": #Esta URL so aceita GET
        return HttpResponse(None, status = 405)

    with open("./database/mailHistory.json") as jsonFile:
        jsonData = json.load(jsonFile)

    return JsonResponse(jsonData, safe = False)

@csrf_exempt
def pair(request): #A funcao de paremento com o celular nao esta sendo utilizada, para nao complicar demais o projeto e demorar muito para ficar pronto
    return HttpResponse("pareamento nao utilizado", status = 501) #Caso receba uma requisicao, responde com codigo HTTP 501
