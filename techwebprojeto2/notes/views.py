import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Note
from .serializers import NoteSerializer
import requests


@api_view(['GET', 'POST'])
def api_maestria(request):
    api_key = 'RGAPI-79e19b55-7c11-4482-bb0e-9cbb7562bfb7'
    riot_api = 'https://br1.api.riotgames.com'
    summoner_api = riot_api + f'/lol/summoner/v4/summoners/by-name/tesujiroqmemame'
    summoner = requests.get(summoner_api, headers={'X-Riot-Token': api_key})
    encryptedSummonerId = summoner.json()['id']
    maestria_api = riot_api + f'/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}'
    maestria = requests.get(maestria_api, headers={'X-Riot-Token': api_key})
    return Response(maestria.json())


@api_view(['GET', 'POST'])
def api_maestria_teste(request, summoner):
    api_key = 'RGAPI-79e19b55-7c11-4482-bb0e-9cbb7562bfb7'
    riot_api = 'https://br1.api.riotgames.com'
    summoner_api = riot_api + f'/lol/summoner/v4/summoners/by-name/{summoner}'
    summoner = requests.get(summoner_api, headers={'X-Riot-Token': api_key})
    encryptedSummonerId = summoner.json()['id']
    maestria_api = riot_api + f'/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}'
    maestria = requests.get(maestria_api, headers={'X-Riot-Token': api_key})
    return Response(maestria.json())


@api_view(['GET', 'POST'])
def api_fav(request):
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid() and len(Note.objects.filter(name=request.data['name'])) == 0:
            serializer.save()
        return Response(serializer.data, status=201)


@api_view(['GET', 'POST', 'DELETE'])
def api_fav_delete(request, champ_id):
    if request.method == 'DELETE':
        note = Note.objects.filter(champ_id=champ_id)
        note.delete()
        return Response(status=204)
