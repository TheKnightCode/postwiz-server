from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time #Todos os tempos estao em fuso horario GMT +0 no formato "%Y/%m/%d %H:%M:%S" (ANO/MES/DIA HORA:MINUTO:SEGUNDO). Este é o mesmo formato usado no arquivo .json
import json

MAX_STATES = 64 #Para evitar que o arquivo mailHistory.json fique infinitamente grande, o numero de estados salvos eh limitado em 64

# Create your views here.
@csrf_exempt #Faz com que o Django evite a verificacao do cookie que evita CSRF. Eu nao sei direito o que eh isso, pode pesquisar se quiser. Sem isso nao funciona
def update(request):
    with open("./database/mailHistory.json", "r") as jsonFile:
        print(request.body)
        jsonData = json.load(jsonFile)
        recievedJson = json.loads(request.body) #Transforma o .json recebido em forma de string para objetos json

        jsonData.insert(0, recievedJson)

        #Remove quaisquer estados antigos que excedem o limite maximo definido por MAX_STATES
        while len(jsonData) > MAX_STATES:
            jsonData.pop(MAX_STATES)

    with open("./database/mailHistory.json", "w") as jsonFile:
        json.dump(jsonData, jsonFile, indent = 4)

    return HttpResponse(jsonData, status = 201)

@csrf_exempt
def code(request): #A funcao de paremento com o celular nao esta sendo utilizada, para nao complicar demais o projeto e demorar muito para ficar pronto
    return HttpResponse("pareamento nao utilizado", status = 501) #Caso receba uma requisicao, responde com codigo HTTP 501
